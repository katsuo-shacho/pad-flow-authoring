# 公式ガイド索引（方法論・仕様）

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/<slug>（CC BY 4.0）。
英語版は ja-jp → en-us。必要な1本だけ WebFetch で読む。各行の語数は読む前の目安。

## 変数・式
- variable-data-types: 変数データ型（テキスト/数値/日時/リスト/データテーブル/カスタムオブジェクト/インスタンス）2.6k語
- datatype-properties: 各データ型のプロパティ（.Count, .RowsCount, .Year など） 2.5k語
- variable-manipulation: `%...%` 記法、演算子、リスト/テーブル添字、`%%`エスケープ 0.9k語
- manage-variables: 変数ペイン、入出力変数、機密変数、既定値 3.2k語
- scoped-variables: サブフロー局所の変数（モジュール化・デバッグ性） 0.8k語
- reserved-keywords: 変数名に使えない予約語 0.2k語
- power-fx: Power Fx対応フロー（Classicとの違い、`=`で始まる式、使える関数） 2.2k語
- natural-language-powerfx: 自然言語→Power Fx式

## 制御・エラー
- use-loops / use-conditionals: ループ・条件分岐の使い方
- errors: エラー処理（アクション単位の「エラー発生時」、ブロックエラー、再試行、ラベルへ移動） 1.2k語
- safe-stop: 安全停止（通常停止との違い、終了処理を確実に走らせる） 0.6k語
- runtime-notifications: 実行時通知の種類

## 設計・品質
- static-analysis: Flow Checker 静的解析ルール（→ 03-principles.md に要約済み） 2.1k語
- test-desktop-flows + actions-reference/testing: テストケース（v2.54+、Premium）。「Test a desktop flow」+「Assert」 0.7k語
- debugging-flow: ブレークポイント、ステップ実行、「ここから実行」 1.0k語
- version-control: バージョン管理（プレビュー、ドラフト/公開/復元） 1.1k語
- designer-workspace / flow-designer: デザイナー構成、サブフロー、アクションのコピー＆貼付（テキストとして共有可）

## UI・Web・画像
- ui-elements: UI要素の取得・セレクター 1.9k語
- build-custom-selectors: カスタムセレクター（属性・`:eq()`・変数埋込） 0.9k語
- automation-web: ブラウザー自動化の基本（拡張機能、要素抽出、JavaScript実行） 1.8k語
- desktop-automation: デスクトップアプリ自動化 0.4k語
- images: 画像ペイン（画像認識） 0.5k語
- ui-elements-fallback-mechanism: UI要素の画像フォールバック 0.6k語
- repair-at-runtime / self-healing: 実行時のセレクター修復（プレビュー）
- create-ui-elements-collections: UI要素コレクションの共有 1.3k語

## 入力UI
- custom-forms: カスタムフォーム（Adaptive Cards。要素ID→ `%CustomFormData['ID']%`、押下ボタン→ `ButtonPressed`。アクションは末尾のみ） 2.2k語
- how-to/handle-custom-forms: ボタンごとの分岐例

## 実行・連携
- run-desktop-flows-url-shortcuts: URL / デスクトップショートカットから実行（`ms-powerautomate:` スキーム、入力変数の受け渡し） 1.2k語
- run-desktop-flows-via-keyboard-shortcuts: キーボードショートカット実行
- trigger-desktop-flows: クラウドフローからの起動
- run-unattended-desktop-flows: 無人実行の条件
- run-desktop-flows-best-practices: 無人実行の負荷分散・タイムアウト（開発原則ではない）
- configure-desktop-flow-logs: ログ詳細度の設定
- troubleshoot: 実行時トラブルシュート 1.3k語

## 保存形式・ALM
- schema / alm-schema: v2スキーマ（ソリューション内のフロー定義） 1.5k語
- console: コンソール（フロー一覧・実行・入力変数の指定）
