# Robin: WorkQueues

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## WorkQueues.BatchEnqueueWorkQueueItems [A]
```
WorkQueues.BatchEnqueueWorkQueueItems EnableParallelProcessing: False WorkQueueItemData: RecognizedEntities WorkQueue: $fx'TestQueue' FailedWorkQueueItems=> FailedWorkQueueItems HasFailedItems=> HasFailedItems SuccessfulWorkQueueItems=> SuccessfulWorkQueueItems
```
入力: !EnableParallelProcessing:Boolean !WorkQueueItemData:DataTable !WorkQueue:WorkQueue
出力: FailedWorkQueueItems:List<BatchEnqueueFailuresResponse>=>FailedWorkQueueItems HasFailedItems:Boolean=>HasFailedItems SuccessfulWorkQueueItems:List<BatchEnqueueSuccessfulResponse>=>SuccessfulWorkQueueItems
ON ERROR可: FailedToBatchEnqueueWorkQueueItemsError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError

### WorkQueues.EnqueueWorkQueueItem のセレクター: WithUniqueId, WithoutUniqueId

## WorkQueues.EnqueueWorkQueueItem.WithUniqueId [A]
```
WorkQueues.EnqueueWorkQueueItem.WithUniqueId ProcessingResult: $fx'example' DelayUntil: $fx'2025-01-01' ThrowOnDuplicateWorkQueueItem: True UniqueId: $fx'example' ExpiryDate: $fx'2025-01-01' Status: WorkQueues.WorkQueueItemEnqueueStatus.Queued WorkQueue: $fx'TestQueue' Priority: WorkQueues.WorkQueueItemPriority.Normal Value: $fx'example' Name: $fx'example' WorkQueueItem=> NewWorkQueueItem
```
入力: ProcessingResult:String DelayUntil:Nullable<DateTime> !ThrowOnDuplicateWorkQueueItem:Boolean UniqueId:String ExpiryDate:Nullable<DateTime> !Status:WorkQueueItemEnqueueStatus{Queued,Paused} !WorkQueue:WorkQueue !Priority:WorkQueueItemPriority{High,Normal,Low} !Value:String Name:String
出力: WorkQueueItem:WorkQueueItem=>NewWorkQueueItem
ON ERROR可: FailedToEnqueueWorkQueueItemError, SchemaValidationInvalidInputError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError
固定: HasUniqueId=True

## WorkQueues.EnqueueWorkQueueItem.WithoutUniqueId [A]
```
WorkQueues.EnqueueWorkQueueItem.WithoutUniqueId ProcessingResult: $fx'example' DelayUntil: $fx'2025-01-01' ThrowOnDuplicateWorkQueueItem: True ExpiryDate: $fx'2025-01-01' Status: WorkQueues.WorkQueueItemEnqueueStatus.Queued WorkQueue: $fx'TestQueue' Priority: WorkQueues.WorkQueueItemPriority.Normal Value: $fx'example' Name: $fx'example' WorkQueueItem=> NewWorkQueueItem
```
入力: ProcessingResult:String DelayUntil:Nullable<DateTime> !ThrowOnDuplicateWorkQueueItem:Boolean ExpiryDate:Nullable<DateTime> !Status:WorkQueueItemEnqueueStatus{Queued,Paused} !WorkQueue:WorkQueue !Priority:WorkQueueItemPriority{High,Normal,Low} !Value:String Name:String
出力: WorkQueueItem:WorkQueueItem=>NewWorkQueueItem
ON ERROR可: FailedToEnqueueWorkQueueItemError, SchemaValidationInvalidInputError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError
固定: HasUniqueId=False

## WorkQueues.GetWorkQueueItems [A]
```
WorkQueues.GetWorkQueueItems RowsToReturn: 5000 ThrowIfWorkQueueNotFound: True WorkQueue: $fx'TestQueue' FilterRows: $fx'example' WorkQueueItems=> WorkQueueItems
```
入力: !RowsToReturn:Int32 !ThrowIfWorkQueueNotFound:Boolean !WorkQueue:WorkQueue !FilterRows:String
出力: WorkQueueItems:List<WorkQueueItem>=>WorkQueueItems
ON ERROR可: FailedToGetWorkQueueItemsError, InvalidFetchXMLError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError

### WorkQueues.ProcessWorkQueueItem のセレクター: ProcessWorkQueueItem, ProcessWorkQueueItemOverrideRetry

## WorkQueues.ProcessWorkQueueItem.ProcessWorkQueueItem [L]
```
LOOP WHILE (WorkQueues.ProcessWorkQueueItem.ProcessWorkQueueItem WorkQueue: $fx'TestQueue' WorkQueueItem=> WorkQueueItem)
```
入力: !WorkQueue:WorkQueue FilterRows:String
出力: WorkQueueItem:WorkQueueItem=>WorkQueueItem
ON ERROR可: FailedToDequeueWorkQueueError, InvalidFetchXMLError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError
固定: IsOverridingAutoRetry=False

## WorkQueues.ProcessWorkQueueItem.ProcessWorkQueueItemOverrideRetry [L]
```
LOOP WHILE (WorkQueues.ProcessWorkQueueItem.ProcessWorkQueueItemOverrideRetry MaxRetryCount: 0 WorkQueue: $fx'TestQueue' FilterRows: $fx'example' WorkQueueItem=> WorkQueueItem)
```
入力: !MaxRetryCount:Int32 !WorkQueue:WorkQueue FilterRows:String
出力: WorkQueueItem:WorkQueueItem=>WorkQueueItem
ON ERROR可: FailedToDequeueWorkQueueError, InvalidFetchXMLError, WorkQueueNotFoundError, WorkQueuePausedOrStoppedError
固定: IsOverridingAutoRetry=True

### WorkQueues.RequeueWorkQueueItem のセレクター: RequeueAndClearProcessingNotes, RequeueWithProcessingNotes

## WorkQueues.RequeueWorkQueueItem.RequeueWithProcessingNotes [A]
```
WorkQueues.RequeueWorkQueueItem.RequeueWithProcessingNotes WorkQueueItem: NewWorkQueueItem DelayUntil: $fx'2025-01-01' ExpiryDate: $fx'2025-01-01' ProcessingResult: $fx'example'
```
入力: WorkQueueItem:WorkQueueItem DelayUntil:DateTime ExpiryDate:Nullable ProcessingResult:String
ON ERROR可: FailedToRequeueWorkQueueItemError, WorkQueueItemNotFoundError, WorkQueueNotFoundError
固定: Clear=False

### WorkQueues.UpdateProcessingNotes のセレクター: ClearProcessingNotes, WithProcessingNotes

## WorkQueues.UpdateProcessingNotes.WithProcessingNotes [A]
```
WorkQueues.UpdateProcessingNotes.WithProcessingNotes WorkQueueItem: NewWorkQueueItem ProcessingNotes: $fx'example'
```
入力: WorkQueueItem:WorkQueueItem ProcessingNotes:String
ON ERROR可: FailedToUpdateProcessingNotesError, WorkQueueItemNotFoundError, WorkQueueNotFoundError
固定: Clear=False

### WorkQueues.UpdateWorkQueueItem のセレクター: UpdateAndClearProcessingNotes, UpdateWithProcessingNotes

## WorkQueues.UpdateWorkQueueItem.UpdateWithProcessingNotes [A]
```
WorkQueues.UpdateWorkQueueItem.UpdateWithProcessingNotes WorkQueueItem: NewWorkQueueItem Status: WorkQueues.WorkQueueItemStatus.Processed InputValue: $fx'example' ProcessingResult: $fx'example'
```
入力: WorkQueueItem:WorkQueueItem Status:WorkQueueItemStatus{Unchanged,Processed,GenericException,ITException,BusinessException,ProcessingTimeout} InputValue:String ProcessingResult:String
ON ERROR可: FailedToUpdateWorkQueueItemError, SchemaValidationInvalidInputError, WorkQueueItemInputUpdateNotAllowedError, WorkQueueItemNotFoundError, WorkQueueItemOnHoldError
固定: Clear=False
