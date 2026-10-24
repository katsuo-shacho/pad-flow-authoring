# Robin: Azure

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 1.1.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

### Azure.AttachDisk のセレクター: AttachManagedDisk, AttachUnManagedDisk

## Azure.AttachDisk.AttachManagedDisk [A]
```
Azure.AttachDisk.AttachManagedDisk AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example' DiskName: $fx'example' DiskResourceGroup: $fx'example'
```
入力: DiskName:String DiskResourceGroup:String ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: DiskNotFoundError, FailedToAttachDiskError, ManagedAndUnManagedDiskNotAllowedTogetherError, VirtualMachineNotFoundError
固定: IsManagedDisk=True

## Azure.AttachDisk.AttachUnManagedDisk [A]
```
Azure.AttachDisk.AttachUnManagedDisk ResourceGroup: $fx'example' VhdName: $fx'example' AzureClient: AzureClient VirtualMachineName: $fx'example' StorageAccount: $fx'example' Container: $fx'example'
```
入力: !ResourceGroup:String !VhdName:String !AzureClient:AzureClient !VirtualMachineName:String !StorageAccount:String !Container:String
ON ERROR可: DiskNotFoundError, FailedToAttachDiskError, ManagedAndUnManagedDiskNotAllowedTogetherError, VirtualMachineNotFoundError
固定: IsManagedDisk=False

### Azure.CreateManagedDisk のセレクター: CreateManagedDisk, CreateManagedDiskFromSnapshot, CreateManagedDiskFromStorageBlob

## Azure.CreateManagedDisk.CreateManagedDisk [A]
```
Azure.CreateManagedDisk.CreateManagedDisk AzureClient: AzureClient DiskName: $fx'example' ResourceGroupCreateOption: Azure.ResourceGroupCreateOption.UseExisting ResourceGroup: $fx'example' Location: $fx'example' SizeInGb: 1 StorageAccountType: Azure.StorageAccountType.Standard AvailabilityZone: $fx'example' ManagedDisk=> ManagedDisk
```
入力: AvailabilityZone:String DiskName:String Location:String ResourceGroup:String ResourceGroupCreateOption:ResourceGroupCreateOption{UseExisting,CreateNew} SizeInGb:Int32 StorageAccountType:StorageAccountType{Standard,Premium,StandardSSD,UltraSSD} AzureClient:AzureClient
出力: ManagedDisk:AzureManagedDisk=>
ON ERROR可: FailedToCreateDiskError, ResourceAlreadyExists, ResourceGroupAlreadyExistsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: Source=None

## Azure.CreateManagedDisk.CreateManagedDiskFromSnapshot [A]
```
Azure.CreateManagedDisk.CreateManagedDiskFromSnapshot SnapshotResourceGroup: $fx'example' SnapshotName: $fx'example' AzureClient: AzureClient StorageAccountType: Azure.StorageAccountType.Standard SizeInGb: 1 DiskName: $fx'example' AvailabilityZone: $fx'example' ResourceGroupCreateOption: Azure.ResourceGroupCreateOption.UseExisting ResourceGroup: $fx'example' Location: $fx'example' ManagedDisk=> ManagedDisk
```
入力: !SnapshotResourceGroup:String !SnapshotName:String !AzureClient:AzureClient !StorageAccountType:StorageAccountType{Standard,Premium,StandardSSD,UltraSSD} !SizeInGb:Int32 !DiskName:String AvailabilityZone:String !ResourceGroupCreateOption:ResourceGroupCreateOption{UseExisting,CreateNew} !ResourceGroup:String !Location:String
出力: ManagedDisk:AzureManagedDisk=>ManagedDisk
ON ERROR可: FailedToCreateDiskError, ResourceAlreadyExists, ResourceGroupAlreadyExistsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: Source=Snapshot

## Azure.CreateManagedDisk.CreateManagedDiskFromStorageBlob [A]
```
Azure.CreateManagedDisk.CreateManagedDiskFromStorageBlob AzureClient: AzureClient StorageAccountType: Azure.StorageAccountType.Standard StorageAccountName: $fx'example' SizeInGb: 1 DiskName: $fx'example' BlobUrl: $fx'example' AvailabilityZone: $fx'example' ResourceGroupCreateOption: Azure.ResourceGroupCreateOption.UseExisting ResourceGroup: $fx'example' Location: $fx'example' ManagedDisk=> ManagedDisk
```
入力: !AzureClient:AzureClient !StorageAccountType:StorageAccountType{Standard,Premium,StandardSSD,UltraSSD} !StorageAccountName:String !SizeInGb:Int32 !DiskName:String !BlobUrl:String AvailabilityZone:String !ResourceGroupCreateOption:ResourceGroupCreateOption{UseExisting,CreateNew} !ResourceGroup:String !Location:String
出力: ManagedDisk:AzureManagedDisk=>ManagedDisk
ON ERROR可: FailedToCreateDiskError, ResourceAlreadyExists, ResourceGroupAlreadyExistsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: Source=StorageBlob

## Azure.CreateResourceGroup [A]
```
Azure.CreateResourceGroup AzureClient: AzureClient GroupName: $fx'example' Location: $fx'example' ResourceGroup=> ResourceGroup
```
入力: GroupName:String Location:String AzureClient:AzureClient
出力: ResourceGroup:AzureResourceGroup=>
ON ERROR可: FailedToCreateResourceGroupError, ResourceGroupAlreadyExistsError

## Azure.CreateSession [A]
```
Azure.CreateSession ClientId: $fx'example' ClientSecret: $fx'password' TenantId: $fx'example' SubscriptionId: $fx'example' AzureClient=> AzureClient
```
入力: ClientId:String ClientSecret:EncryptableObject SubscriptionId:String TenantId:String
出力: AzureClient:AzureClient=>
ON ERROR可: FailedToCreateAzureClientError

## Azure.CreateSnapshot [A]
```
Azure.CreateSnapshot AzureClient: AzureClient SnapshotName: $fx'example' ResourceGroupCreateOption: Azure.ResourceGroupCreateOption.UseExisting ResourceGroup: $fx'example' Location: $fx'example' DiskName: $fx'example' DiskResourceGroup: $fx'example' Snapshot=> Snapshot
```
入力: DiskName:String DiskResourceGroup:String Location:String ResourceGroup:String ResourceGroupCreateOption:ResourceGroupCreateOption{UseExisting,CreateNew} SnapshotName:String AzureClient:AzureClient
出力: Snapshot:AzureSnapshot=>Snapshot
ON ERROR可: DiskNotFoundError, FailedToCreateSnapshotError, ResourceAlreadyExists, ResourceGroupAlreadyExistsError, ResourceGroupNotFoundError

## Azure.DeleteDisk [A]
```
Azure.DeleteDisk AzureClient: AzureClient DiskName: $fx'example' ResourceGroup: $fx'example'
```
入力: DiskName:String ResourceGroup:String AzureClient:AzureClient
ON ERROR可: AttachedToVirtualMachineError, DiskNotFoundError, FailedToDeleteDiskError, ResourceGroupNotFoundError

## Azure.DeleteResourceGroup [A]
```
Azure.DeleteResourceGroup AzureClient: AzureClient GroupName: $fx'example'
```
入力: GroupName:String AzureClient:AzureClient
ON ERROR可: FailedToDeleteResourceGroupsError

## Azure.DeleteSnapshot [A]
```
Azure.DeleteSnapshot AzureClient: AzureClient SnapshotName: $fx'example' ResourceGroup: $fx'example'
```
入力: ResourceGroup:String SnapshotName:String AzureClient:AzureClient
ON ERROR可: FailedToDeleteSnapshotError, ResourceGroupNotFoundError, SnapshotNotFoundError

### Azure.DescribeVirtualMachine のセレクター: DescribeAllVirtualMachines, DescribeVirtualMachinesByName, DescribeVirtualMachinesByNameAndResourceGroup, DescribeVirtualMachinesByResourceGroup

## Azure.DescribeVirtualMachine.DescribeAllVirtualMachines [A]
```
Azure.DescribeVirtualMachine.DescribeAllVirtualMachines AzureClient: AzureClient Status: Azure.VMStatus.Any VirtualMachines=> VirtualMachines
```
入力: Status:VMStatus{Running,Deallocating,Deallocated,Starting,Stopped,Stopping,Unknown,Any} AzureClient:AzureClient
出力: VirtualMachines:List=>
ON ERROR可: FailedToDescribeVirtualMachinesError, ResourceGroupNotFoundError, VirtualMachineNotFoundError
固定: RetrieveVMMode=All

## Azure.DescribeVirtualMachine.DescribeVirtualMachinesByName [A]
```
Azure.DescribeVirtualMachine.DescribeVirtualMachinesByName VirtualMachineName: $fx'example' AzureClient: AzureClient Status: Azure.VMStatus.Any VirtualMachines=> VirtualMachines
```
入力: !VirtualMachineName:String !AzureClient:AzureClient !Status:VMStatus{Running,Deallocating,Deallocated,Starting,Stopped,Stopping,Unknown,Any}
出力: VirtualMachines:List<AzureVirtualMachine>=>VirtualMachines
ON ERROR可: FailedToDescribeVirtualMachinesError, ResourceGroupNotFoundError, VirtualMachineNotFoundError
固定: RetrieveVMMode=ByName

## Azure.DescribeVirtualMachine.DescribeVirtualMachinesByNameAndResourceGroup [A]
```
Azure.DescribeVirtualMachine.DescribeVirtualMachinesByNameAndResourceGroup VirtualMachineName: $fx'example' AzureClient: AzureClient Status: Azure.VMStatus.Any ResourceGroup: $fx'example' VirtualMachines=> VirtualMachines
```
入力: !VirtualMachineName:String !AzureClient:AzureClient !Status:VMStatus{Running,Deallocating,Deallocated,Starting,Stopped,Stopping,Unknown,Any} !ResourceGroup:String
出力: VirtualMachines:List<AzureVirtualMachine>=>VirtualMachines
ON ERROR可: FailedToDescribeVirtualMachinesError, ResourceGroupNotFoundError, VirtualMachineNotFoundError
固定: RetrieveVMMode=ByResourceGroupAndName

## Azure.DescribeVirtualMachine.DescribeVirtualMachinesByResourceGroup [A]
```
Azure.DescribeVirtualMachine.DescribeVirtualMachinesByResourceGroup AzureClient: AzureClient Status: Azure.VMStatus.Any ResourceGroup: $fx'example' VirtualMachines=> VirtualMachines
```
入力: !AzureClient:AzureClient !Status:VMStatus{Running,Deallocating,Deallocated,Starting,Stopped,Stopping,Unknown,Any} !ResourceGroup:String
出力: VirtualMachines:List<AzureVirtualMachine>=>VirtualMachines
ON ERROR可: FailedToDescribeVirtualMachinesError, ResourceGroupNotFoundError, VirtualMachineNotFoundError
固定: RetrieveVMMode=ByResourceGroup

## Azure.DetachDisk [A]
```
Azure.DetachDisk AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example' DiskName: $fx'example'
```
入力: DiskName:String ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: FailedToDetachDiskError, NotAttachedToVirtualMachineError, ResourceGroupNotFoundError, VirtualMachineNotFoundError

## Azure.EndSession [A]
```
Azure.EndSession AzureClient: AzureClient
```
入力: AzureClient:AzureClient
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

### Azure.GetDisks のセレクター: GetAllDisks, GetDisksByName, GetDisksByNameAndResourceGroup, GetDisksByResourceGroup

## Azure.GetDisks.GetAllDisks [A]
```
Azure.GetDisks.GetAllDisks AzureClient: AzureClient Disks=> Disks
```
入力: AzureClient:AzureClient
出力: Disks:List=>
ON ERROR可: DiskNotFoundError, FailedToGetDisksError, ResourceGroupNotFoundError
固定: RetrieveDisksMode=All

## Azure.GetDisks.GetDisksByName [A]
```
Azure.GetDisks.GetDisksByName AzureClient: AzureClient DiskName: $fx'example' Disks=> Disks
```
入力: !AzureClient:AzureClient !DiskName:String
出力: Disks:List<AzureManagedDisk>=>Disks
ON ERROR可: DiskNotFoundError, FailedToGetDisksError, ResourceGroupNotFoundError
固定: RetrieveDisksMode=ByName

## Azure.GetDisks.GetDisksByNameAndResourceGroup [A]
```
Azure.GetDisks.GetDisksByNameAndResourceGroup AzureClient: AzureClient DiskName: $fx'example' ResourceGroup: $fx'example' Disks=> Disks
```
入力: !AzureClient:AzureClient !DiskName:String !ResourceGroup:String
出力: Disks:List<AzureManagedDisk>=>Disks
ON ERROR可: DiskNotFoundError, FailedToGetDisksError, ResourceGroupNotFoundError
固定: RetrieveDisksMode=ByResourceGroupAndName

## Azure.GetDisks.GetDisksByResourceGroup [A]
```
Azure.GetDisks.GetDisksByResourceGroup AzureClient: AzureClient ResourceGroup: $fx'example' Disks=> Disks
```
入力: !AzureClient:AzureClient !ResourceGroup:String
出力: Disks:List<AzureManagedDisk>=>Disks
ON ERROR可: DiskNotFoundError, FailedToGetDisksError, ResourceGroupNotFoundError
固定: RetrieveDisksMode=ByResourceGroup

## Azure.GetResourceGroups [A]
```
Azure.GetResourceGroups AzureClient: AzureClient GroupName: $fx'example' ResourceGroups=> ResourceGroups
```
入力: GroupName:String AzureClient:AzureClient
出力: ResourceGroups:List=>
ON ERROR可: FailedToGetResourceGroupsError

### Azure.GetSnapshots のセレクター: GetAllSnapshots, GetSnapshotsByName, GetSnapshotsByNameAndResourceGroup, GetSnapshotsByResourceGroup

## Azure.GetSnapshots.GetAllSnapshots [A]
```
Azure.GetSnapshots.GetAllSnapshots AzureClient: AzureClient Snapshots=> Snapshots
```
入力: AzureClient:AzureClient
出力: Snapshots:List=>
ON ERROR可: FailedToGetSnapshotsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: RetrieveSnapshotsMode=All

## Azure.GetSnapshots.GetSnapshotsByName [A]
```
Azure.GetSnapshots.GetSnapshotsByName SnapshotName: $fx'example' AzureClient: AzureClient Snapshots=> Snapshots
```
入力: !SnapshotName:String !AzureClient:AzureClient
出力: Snapshots:List<AzureSnapshot>=>Snapshots
ON ERROR可: FailedToGetSnapshotsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: RetrieveSnapshotsMode=ByName

## Azure.GetSnapshots.GetSnapshotsByNameAndResourceGroup [A]
```
Azure.GetSnapshots.GetSnapshotsByNameAndResourceGroup SnapshotName: $fx'example' AzureClient: AzureClient ResourceGroup: $fx'example' Snapshots=> Snapshots
```
入力: !SnapshotName:String !AzureClient:AzureClient !ResourceGroup:String
出力: Snapshots:List<AzureSnapshot>=>Snapshots
ON ERROR可: FailedToGetSnapshotsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: RetrieveSnapshotsMode=ByResourceGroupAndName

## Azure.GetSnapshots.GetSnapshotsByResourceGroup [A]
```
Azure.GetSnapshots.GetSnapshotsByResourceGroup AzureClient: AzureClient ResourceGroup: $fx'example' Snapshots=> Snapshots
```
入力: !AzureClient:AzureClient !ResourceGroup:String
出力: Snapshots:List<AzureSnapshot>=>Snapshots
ON ERROR可: FailedToGetSnapshotsError, ResourceGroupNotFoundError, SnapshotNotFoundError
固定: RetrieveSnapshotsMode=ByResourceGroup

## Azure.GetSubscriptions [A]
```
Azure.GetSubscriptions AzureClient: AzureClient Subscriptions=> Subscriptions
```
入力: AzureClient:AzureClient
出力: Subscriptions:List=>
ON ERROR可: FailedToGetSubscriptionsError

## Azure.GetVirtualMachines [A]
```
Azure.GetVirtualMachines AzureClient: AzureClient Status: Azure.VMStatus.Any ResourceGroup: $fx'example' VirtualMachinesInfo=> VirtualMachinesInfo
```
入力: ResourceGroup:String Status:VMStatus{Running,Deallocating,Deallocated,Starting,Stopped,Stopping,Unknown,Any} AzureClient:AzureClient
出力: VirtualMachinesInfo:List=>
ON ERROR可: FailedToGetVirtualMachinesError, ResourceGroupNotFoundError

## Azure.RestartVirtualMachine [A]
```
Azure.RestartVirtualMachine AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example'
```
入力: ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: FailedToRestartVirtualMachineError, ResourceGroupNotFoundError, VirtualMachineNotFoundError

## Azure.ShutDownVirtualMachine [A]
```
Azure.ShutDownVirtualMachine AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example'
```
入力: ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: FailedToShutDownVirtualMachineError, ResourceGroupNotFoundError, VirtualMachineNotFoundError

## Azure.StartVirtualMachine [A]
```
Azure.StartVirtualMachine AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example'
```
入力: ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: FailedToStartVirtualMachineError, ResourceGroupNotFoundError, VirtualMachineNotFoundError

## Azure.StopVirtualMachine [A]
```
Azure.StopVirtualMachine AzureClient: AzureClient VirtualMachineName: $fx'example' ResourceGroup: $fx'example'
```
入力: ResourceGroup:String VirtualMachineName:String AzureClient:AzureClient
ON ERROR可: FailedToStopVirtualMachineError, ResourceGroupNotFoundError, VirtualMachineNotFoundError
