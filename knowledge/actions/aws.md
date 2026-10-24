# AWS actions actions reference

出典: https://learn.microsoft.com/ja-jp/power-automate/desktop-flows/actions-reference/aws （Microsoft Docs, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/ — 本プロジェクトによる要約・圧縮。Microsoft の見解ではない。LEGAL.md 参照）

概要: Power Automate enables users to handle EC2 instances, volumes, and snapshots through the AWS group of actions. Before deploying any AWS action, create a new EC2 session using the Create EC2 session action. To use a credentials file for authentication, disable Access keys and populate Profile name and Profile location. If you don't want to reference a profile name explicitly, choose default in Profile name to use the default profile. Alternatively, enable Access keys and populate the access key ID, the secret access key, and the region constraint specifying the endpoint. After creating the sess

## Start EC2 instance  `#startec2instance`
Start EC2 instance(s).
入力:
- EC2 client: EC2 client — The EC2 client
- Instance IDs: List of Text values — The instance IDs to start
出力:
- StartingEc2Instances: List of Instance state changes — The returned information for the started instances
例外: Authentication failed; Unauthorized operation; Invalid instance ID; Insufficient capacity; Amazon service request failed

## Stop EC2 instance  `#stopec2instance`
Stop EC2 instance(s).
入力:
- EC2 client: EC2 client — The EC2 client
- Instance IDs: List of Text values — The instance IDs to stop
- Force stop: Boolean value = False — Specifies whether to force the instances to stop. The instances don't have an opportunity to flush file system caches or file system metadata
- Hibernation:: Boolean value = False — Specifies whether to hibernate the instance, if it was enabled for hibernation at launch. If the instance can't hibernate successfully, a normal shutdown occurs
出力:
- StoppingEc2Instances: List of Instance state changes — The returned information for the stopped instances
例外: Authentication failed; Unauthorized operation; Unsupported operation; Invalid instance ID; Amazon service request failed

## Reboot EC2 instance  `#rebootec2instance`
Reboot EC2 instance(s).
入力:
- EC2 client: EC2 client — The EC2 client
- Instance IDs: List of Text values — The instance IDs to reboot
例外: Authentication failed; Unauthorized operation; Unsupported operation; Invalid instance ID; Incorrect state for the request; Amazon service request failed

## Get available EC2 instances  `#getavailableec2instances`
Get information for the relevant EC2 instances.
入力:
- EC2 client: EC2 client — The EC2 client
- Availability zone(任意): Text value — Specifies the availability zone, a region code followed by a letter identifier
- Instance state: Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped = All — The state of the instance (pending, running, shutting down, terminated, stopping, stopped)
出力:
- Ec2InstancesInfo: List of EC2 instances info — The list of the EC2 instances
例外: Authentication failed; Unauthorized operation; Amazon service request failed

## Describe instances  `#describeec2instance`
Returns all the information for the specified EC2 instance(s).
入力:
- EC2 client: EC2 client — The EC2 client
- Instance IDs(任意): List of Text values — The instance IDs to describe
- Availability zone(任意): Text value — Specifies the availability zone, a region code followed by a letter identifier
- Instance state: Pending, All, Unknown, Running, Shutting down, Terminated, Stopping, Stopped = All — The current state of the instance
出力:
- Ec2Instances: List of EC2 instances — The retrieved instance(s) with all the relevant information
例外: Authentication failed; Unauthorized operation; Invalid instance ID; Amazon service request failed

## Create snapshot  `#createsnapshot`
Create a snapshot of an EBS volume and stores it in Amazon S3.
入力:
- EC2 client: EC2 client — The EC2 client
- Volume ID: Text value — The ID of the EBS volume
- Name(任意): Text value — The name of the snapshot
- Description(任意): Text value — A description for the snapshot
- Purpose(任意): Text value — The purpose of the snapshot
出力:
- Snapshot: EBS snapshot — The created snapshot
例外: Authentication failed; Unauthorized operation; Invalid volume; Resource's limit is exceeded; Amazon service request failed

## Describe snapshots  `#describesnapshots`
Describes the specified EBS snapshots available.
入力:
- EC2 client: EC2 client — The EC2 client
- Describe snapshots mode: All snapshots, Snapshots by ID, Snapshots by owner ID, Snapshots by restorable user ID, Snapshots by custom filter = All snapshots — Specifies whether to get all snapshots of the defined region or filter snapshots by their ID, owner, or user by which they're restorable
- Snapshot IDs(任意): List of Text values — The snapshot IDs to describe
- Owner IDs(任意): List of Text values — The owner IDs who own the snapshots
- Restorable by user IDs(任意): List of Text values — The IDs of the AWS accounts that can create volumes from the snapshot
出力:
- EBSSnapshots: List of EBS snapshots — The retrieved snapshot(s) with all the relevant information
例外: Authentication failed; Unauthorized operation; Invalid snapshot ID; Invalid user ID; Amazon service request failed

## Delete snapshot  `#deletesnapshot`
Delete the specified snapshot.
入力:
- EC2 client: EC2 client — The EC2 client
- Snapshot ID: Text value — The ID of the EBS snapshot to delete
例外: Authentication failed; Unauthorized operation; Invalid snapshot ID; The resource is in use; Amazon service request failed

## Create volume  `#createvolumeaction`
Create an EBS volume.
入力:
- EC2 client: EC2 client — The EC2 client
- Name(任意): Text value — The desired name for the volume
- Purpose(任意): Text value — The purpose of the volume, if any
- Availability zone: Text value — Specifies the availability zone, a region code followed by a letter identifier
- From snapshot: Boolean value = False — Specifies whether to create the volume from a specified snapshot
- Snapshot ID: Text value — The snapshot from to create the volume from
- Volume size: Text value — The size of the volume in GBs
- Size(任意): Text value — The size must be equal to or larger than the snapshot size
- Encrypted: Boolean value = False — Specifies whether to encrypt the volume
- Volume type: Gp2, Standard, Io1, Sc1, St1 = Gp2 — The type of the volume
出力:
- Volume: EBS volume — The created volume
例外: Authentication failed; Unauthorized operation; Invalid parameter; Invalid zone; Resource's limit is exceeded; Volume type isn't supported in the specified zone; Amazon service request failed

## Attach volume  `#attachvolume`
Attach an EBS volume to an EC2 instance.
入力:
- EC2 client: EC2 client — The EC2 client
- Volume ID: Text value — The ID of the EBS volume
- Instance ID: Text value — The ID of the instance
- Device name: Text value — The name of the device
例外: Authentication failed; Unauthorized operation; Unsupported operation; Invalid parameter; Invalid volume; The resource is in use; Amazon service request failed

## Detach volume  `#detachvolume`
Detach an EBS volume from an EC2 instance.
入力:
- EC2 client: EC2 client — The EC2 client
- Volume ID: Text value — The ID of the EBS volume
- Instance ID(任意): Text value — The ID of the instance
- Device name(任意): Text value — The name of the device
- Force detachment: Boolean value = False — Specifies whether to force detachment, if the previous detachment attempt didn't occur cleanly
例外: Authentication failed; Unauthorized operation; Unsupported operation; Invalid parameter; Invalid attempt to detach; Incorrect state for the request; Amazon service request failed

## Describe volumes  `#describevolumes`
Describe the specified EBS volumes.
入力:
- EC2 client: EC2 client — The EC2 client
- Describe volumes mode: All volumes, Volumes of the specified instance, Volumes with the specified IDs = All volumes — Specifies whether to describe all volumes, volumes specified by ID or volumes of an instance
- Volume IDs: List of Text values — The volume IDs to describe
- Instance ID: Text value — The ID of the instance that the volume is attached to
出力:
- EBSVolumes: List of EBS volumes — The retrieved EBS volumes with all the relevant information
例外: Authentication failed; Unauthorized operation; Invalid parameter; Amazon service request failed

## Delete volume  `#deletevolume`
Delete the specified EBS volume.
入力:
- EC2 client: EC2 client — The EC2 client
- Volume ID: Text value — The ID of the EBS volume to delete
例外: Authentication failed; Unauthorized operation; Invalid parameter; Invalid volume; Incorrect state for the request; The resource is in use; Amazon service request failed

## Create EC2 session  `#createec2sessionaction`
Create an EC2 client to automate EC2 web services.
入力:
- Access keys: Boolean value = False — Specifies whether to use access key ID and secret access key in order to create the EC2 session
- Access key ID: Text value — The AWS access key ID
- Secret: Direct encrypted input or Text value — The AWS secret access key
- Region endpoint: Text value — The region constant to use that determines the endpoint to use
- Profile name: Text value = default — The name of the profile to use
- Profile location(任意): Text value — The location of the credentials file that contains the profile to use
出力:
- Ec2Client: EC2 client — The EC2 client
例外: Profile doesn't exist; Invalid profile; Create session failed

## End EC2 session  `#endec2session`
Dispose an open EC2 client.
入力:
- EC2 client: EC2 client — The EC2 client
