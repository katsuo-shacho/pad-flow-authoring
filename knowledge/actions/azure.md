# Azure actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/azure （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate allows you to manage Azure virtual machines through the Azure group of actions. To implement Azure functionality in your desktop flows, create a new Azure session using the Create session action. This action requires you to enter the Client ID, an authentication key for the specific application, and the respective password. Additionally, enter the Tenant ID that is the Microsoft Entra in which you've created the application. Lastly, populate the appropriate Subscription ID. The subscription ID is a GUID that uniquely identifies your subscription to Azure services. After creating

## Get resource groups  `#getresourcegroups`
Gets the resource groups based on the specified criteria.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Resource group name(任意): Text value — The name of the resource group
出力:
- ResourceGroups: List of Azure resource groups — The retrieved resource groups
例外: Failed to get the resource groups with the specified criteria

## Create resource group  `#createresourcegroup`
Creates a new resource group.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Resource group name: Text value — The name of the resource group
- Location: Text value — The location where the new disk will be created
出力:
- ResourceGroup: Azure resource group — The created resource group
例外: Resource group already exists; Failed to create resource group

## Delete resource group  `#deleteresourcegroup`
Deletes the specified resource group and all the contained resources.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Resource group name: Text value — The name of the resource group
例外: Failed to delete the resource group

## Get disks  `#getdisksaction`
Gets the disks based on the specified criteria.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Retrieve disks: All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group = All — Specify which disks to retrieve
- Resource group: Text value — The resource group where the disks reside
- Disk name: Text value — The name of the disk
出力:
- Disks: List of Azure managed disks — The retrieved disks with all the related information
例外: Disk wasn't found; Resource group wasn't found; Failed to get the disks with the specified criteria

## Attach disk  `#attachdisk`
Attaches an existing disk to the virtual machine with the specified name and resource group.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The VM where the disk will be attached
- VM resource group: Text value — The resource group of the VM
- Disk is managed: Boolean value = True — Specify whether the disk to attach is managed
- Disk name: Text value — The name of the disk to attach
- Disk's resource group: Text value — The resource group of the disk
- Storage account: Text value — The storage account where VHD file is located
- Container: Text value — The container that holds the VHD file
- VHD file: Text value — The name of the VHD file
例外: VM wasn't found; Disk wasn't found; Both unmanaged and managed disk can't exist together in a VM; Failed to attach the disk

## Detach disk  `#detachdisk`
Detaches the disk from the virtual machine with the specified name and resource group.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The VM from where the disk will be detached
- Virtual machine's resource group: Text value — The resource group of the VM
- Disk name: Text value — The name of the disk to detach
- Disk is managed: Boolean value = True — Specify whether the disk to detach is managed
例外: VM wasn't found; Failed to detach because the disk isn't attached to the specified VM; Failed to detach disk

## Create managed disk  `#createmanageddiskaction`
Creates a managed disk with the specified settings.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Disk name: Text value — The name of the managed disk to create
- Resource group option: Use existing, Create new = Use existing — Specify whether a new resource group will be created or an existing one will be used
- Resource group name: Text value — The resource group of the disk
- Location: Text value — The location where the new disk is created
- Source type: None, Snapshot, Storage blob = None — Specifies whether to create an empty disk or use the snapshot of another disk or use a blob in a storage account
- Snapshot name: Text value — The managed snapshot to use as a source
- Snapshot's resource group: Text value — The resource group of the snapshot
- Blob URL: Text value — The URL of the blob
- Disk size in GB: Numeric value — Size of the disk in GB
- Storage account type: Standard HDD, Premium SSD, Standard SSD, Ultra disk SSD = Standard HDD — The disk type
- Storage account name: Text value — The name of the storage account where VHD file is stored
- Availability zone(任意): Text value — The availability zone for the managed disk
出力:
- ManagedDisk: Azure managed disk — The created managed disk
例外: Resource group already exists; Resource group wasn't found; The resource with the specified name already exists; Snapshot wasn't found; Failed to create disk

## Delete disk  `#deletedisk`
Deletes the managed disk with the specified name and resource group.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Disk name: Text value — The name of the managed disk to delete
- Resource group: Text value — The resource group of the disk
例外: Disk wasn't found; Failed to delete the disk because it's attached to a VM; Failed to delete disk

## Get snapshots  `#getsnapshotsaction`
Gets the snapshots based on the specified criteria.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Retrieve snapshots: All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group = All — Specify which snapshots to retrieve
- Resource group: Text value — The resource group where the snapshots reside
- Snapshot name: Text value — The name of the snapshot
出力:
- Snapshots: List of Azure snapshots — The retrieved snapshots with all the related information
例外: Snapshot wasn't found; Resource group wasn't found; Failed to get the snapshots with the specified criteria

## Create snapshot  `#createsnapshot`
Creates a snapshot from the specified disk.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Snapshot name: Text value — The name of the snapshot to create
- Resource group option: Use existing, Create new = Use existing — Specifies whether a new resource group will be created or an existing one will be used
- Resource group: Text value — The resource group where the snapshot will be created
- Location: Text value — The location where the new disk will be created
- Source disk: Text value — The name of the managed disk that will be used as source data
- Source disk's resource group: Text value — The resource group of the managed disk that will be used as source data
出力:
- Snapshot: Azure snapshot — The created snapshot
例外: Resource group already exists; Resource group wasn't found; The resource with the specified name already exists; Disk wasn't found; Failed to create snapshot

## Delete snapshot  `#deletesnapshot`
Deletes the snapshot with the specified name and resource group.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Snapshot name: Text value — The name of the snapshot to delete
- Resource group: Text value — The resource group of the snapshot
例外: Snapshot wasn't found; Failed to delete snapshot

## Get virtual machines  `#getvirtualmachines`
Gets the basic information for the virtual machines.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Resource group(任意): Text value — The resource group of the virtual machine
- Status: Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any = Any — The status of the virtual machine
出力:
- VirtualMachinesInfo: List of Azure virtual machine info — The retrieved virtual machines with basic information
例外: Resource group wasn't found; Failed to get the VMs with basic information

## Describe virtual machine  `#describevirtualmachineaction`
Gets all the information for the virtual machine(s) based on the specified criteria.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Describe virtual machines: All, With the specified resource group, With the specified name in all resource groups, With specific name in the specified resource group = All — Specify which virtual machines to describe
- Resource group: Text value — The resource group of the virtual machine
- Virtual machine name: Text value — The name of the virtual machine
- Status: Running, Deallocating, Deallocated, Starting, Stopped, Stopping, Unknown, Any = Any — The status of the virtual machine
出力:
- VirtualMachines: List of Azure virtual machines — The retrieved virtual machines with all the related information
例外: VM wasn't found; Resource group wasn't found; Failed to get basic information of the VM(s)

## Start virtual machine  `#startvirtualmachine`
Starts the virtual machine.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The name of the virtual machine
- Resource group: Text value — The resource group of the virtual machine
例外: VM wasn't found; Failed to start the VM

## Stop virtual machine  `#stopvirtualmachine`
Stops the virtual machine and delocates the related hardware (CPU and memory) and network resources.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The name of the virtual machine
- Resource group: Text value — The resource group of the virtual machine
例外: VM wasn't found; Failed to stop the VM

## Shut down virtual machine  `#shutdownvirtualmachine`
Shuts down the operating system of a virtual machine.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The name of the virtual machine
- Resource group: Text value — The resource group of the virtual machine
例外: VM wasn't found; Failed to shut down the VM

## Restart virtual machine  `#restartvirtualmachine`
Restarts a virtual machine.
入力:
- Azure client: Azure client — The client used to connect to Azure
- Virtual machine name: Text value — The name of the virtual machine
- Resource group: Text value — The resource group of the virtual machine
例外: VM wasn't found; Failed to restart the VM

## Create session  `#createsessionaction`
Creates an Azure session.
入力:
- Client ID: Text value — The client ID of the application, also known as application ID, which identifies the application that is using the token
- Client secret: Direct encrypted input or Text value — The secret for the client ID
- Tenant ID: Text value — The directory ID of the Microsoft Entra
- Subscription ID(任意): Text value — The Azure subscription ID. If not provided, the default subscription will be used
出力:
- AzureClient: Azure client — The created Azure client
例外: Failed to create Azure client

## Get subscriptions  `#getsubscriptions`
Gets subscriptions that the current account can access.
入力:
- Azure client: Azure client — The client used to connect to Azure
出力:
- Subscriptions: List of Azure subscriptions — The retrieved subscriptions with all the related information
例外: Failed to get the subscriptions with the specified criteria

## End session  `#endsession`
Ends an Azure session.
入力:
- Azure client: Azure client — The client used to connect to Azure
