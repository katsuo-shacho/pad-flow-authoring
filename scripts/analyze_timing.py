#!/usr/bin/env python3
"""
analyze_timing.py — 実行ログから区間時間を出し、待機を除いた純処理時間で重い区間を優先度順に並べる

入力: 1行に「時刻 ラベル」。時刻は HH:MM:SS(.fff) か ISO 形式。PAD の実行ログ（アクション開始時刻）や
      DateTime.GetCurrentDateTime で書いたログをそのまま貼れる。ラベルに WAIT / 待機 / Wait for / ダイアログ を含む行は待機扱い。
使い方: python3 analyze_timing.py run.log [--top 10]
出力: 粗い区間表（連続する同じ接頭辞＝区間）→ 上位区間の内訳（細かく見るべき場所）→ 優先度付き提案の雛形
"""
import sys, re, pathlib, collections
TS = re.compile(r"(\d{4}-\d{2}-\d{2}[ T])?(\d{1,2}):(\d{2}):(\d{2})(?:[.,](\d{1,3}))?")
WAITY = re.compile(r"\bWAIT\b|待機|Wait for|ダイアログ|dialog", re.I)
def parse(path):
    rows = []
    for ln in pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        m = TS.search(ln)
        if not m: continue
        h, mi, s, ms = int(m.group(2)), int(m.group(3)), int(m.group(4)), int((m.group(5) or "0").ljust(3, "0"))
        t = h*3600 + mi*60 + s + ms/1000
        label = (ln[:m.start()] + ln[m.end():]).strip(" \t|,;-") or "(no label)"
        rows.append((t, label))
    return rows
def main():
    args = sys.argv[1:]; top = 10
    if "--top" in args: top = int(args[args.index("--top")+1])
    rows = parse(args[0])
    if len(rows) < 2: print("時刻付きの行が2行以上必要"); return
    durs = []
    for (t, l), (t2, _) in zip(rows, rows[1:]):
        d = t2 - t
        if d < 0: d += 86400
        durs.append((d, l, bool(WAITY.search(l))))
    total = sum(d for d, _, _ in durs); wait = sum(d for d, _, w in durs if w)
    print(f"合計 {total:.1f}s  うち待機 {wait:.1f}s  純処理 {total-wait:.1f}s  ({len(durs)} ステップ)")
    # coarse: group by first word / prefix before ':' or '.'
    seg = collections.OrderedDict()
    for d, l, w in durs:
        key = re.split(r"[:.\s]", l, maxsplit=1)[0] or l
        a = seg.setdefault(key, [0.0, 0.0, 0]); a[0] += d; a[1] += d if w else 0; a[2] += 1
    print("\n== 粗い区間（純処理時間順）")
    for k, (d, wd, n) in sorted(seg.items(), key=lambda kv: -(kv[1][0]-kv[1][1]))[:top]:
        print(f"  {d-wd:8.1f}s 純処理 | {wd:6.1f}s 待機 | {n:4d} 回 | {k}")
    print("\n== 重いステップ（純処理、上位）")
    for d, l, w in sorted((x for x in durs if not x[2]), key=lambda x: -x[0])[:top]:
        print(f"  {d:8.1f}s | {l[:90]}")
    print("\n== 提案の雛形（優先度 = 時間×回数）")
    for i, (k, (d, wd, n)) in enumerate(sorted(seg.items(), key=lambda kv: -(kv[1][0]-kv[1][1]))[:3], 1):
        print(f"  {i}. [{'高' if i==1 else '中'}] 区間「{k}」: 純処理 {d-wd:.1f}s / {n}回 → 一括化・ループ内削減・スクリプト化のどれが効くか。期待効果／リスク／戻し方を添える")
if __name__ == "__main__": main()
