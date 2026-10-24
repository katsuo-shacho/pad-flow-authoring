# Work queues actions

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/workqueues （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Work Queues in Power Automate can be used to store process-relevant data and provide a way to decouple complex processes and automations, allowing them to communicate asynchronously. Work queues can play a crucial role in improving the efficiency, scalability, and resiliency of automations and help prioritize work. Work queues allow you to complete highest-priority items first, regardless of whether they're processed by digital workers, human workers, or through integrations.

## Process work queue items
The Process work queue items action indicates to the queue orchestrator that the machine is ready to process one or more work queue items. The user context requesting a new item needs to have sufficient privileges on the work queue and work queue items table in order to process work queues.

## Update work queue item
The Update work queue item action allows users to change the status and processing results of the selected work queue item.

## Add work queue item
The Add work queue item action allows users to populate work queue items into a work queue, which has been set up in the flow portal.

## Add multiple work queue items
The Add multiple work queue items action allows users to add one or more work queue items to a work queue based on the data provided as work queue item data table.

## Requeue item with delay
The Requeue item with delay action allows users to readd a queue item being processed in the desktop flow, back into its originating queue. In addition, the queued item can be held and released until a defined time.

## Update work queue item processing notes
The Update work queue item processing notes action allows users to update or clear processing notes of the selected work queue item without changing its state or any other property.

## Get work queue items by filter
The Get work queue items by filter action allows users to retrieve one or more work queue items based on a FetchXML filter expression.

## Related information
- Work queue overview
