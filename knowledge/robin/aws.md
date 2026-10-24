# Robin: AWS

出典: PAD Robin Action Knowledge Base (Joe Green, CC BY 4.0) https://github.com/JoeG592/pad-robin-action-kb — 要約・圧縮して再構成。License: https://creativecommons.org/licenses/by/4.0/
ここにある ID・引数名・enum・エラー名は、PAD デザイナーで観察された製品の挙動の記録であり、Microsoft の資料の複製ではない（LEGAL.md）。
KB 3.4.0 / PAD 2.73.00155.26278 / 2026-10-17

各項目: ID [kind] / 例（貼付検証済み） / 入力 name:type（!=必須, {enum}） / 出力 / エラー名。同じ家族のセレクター一覧は ### 行

## AWS.AttachVolume [A]
```
AWS.AttachVolume Ec2Client: Ec2Client VolumeId: $'''example''' InstanceId: $'''example''' Device: $'''example'''
```
入力: Device:String InstanceId:String VolumeId:String Ec2Client:Ec2ClientObject
ON ERROR可: AuthenticationFailureError, InvalidParameterError, InvalidVolumeError, RequestFailedError, ResourceIsInUseError, UnauthorizedOperationError, UnsupportedOperationError

### AWS.CreateEc2Session のセレクター: CreateEc2SessionWithAccessKeys, CreateEc2SessionWithProfile

## AWS.CreateEc2Session.CreateEc2SessionWithAccessKeys [A]
```
AWS.CreateEc2Session.CreateEc2SessionWithAccessKeys RegionEndpoint: $'''example''' Secret: $'''password''' AccessKeyId: $'''example''' Ec2Client=> Ec2Client
```
入力: !RegionEndpoint:String !Secret:EncryptableObject !AccessKeyId:String
出力: Ec2Client:Ec2ClientObject=>Ec2Client
ON ERROR可: CreateSessionFailed, InvalidProfileError, ProfileNotFoundError
固定: UseAccessKeys=True

## AWS.CreateEc2Session.CreateEc2SessionWithProfile [A]
```
AWS.CreateEc2Session.CreateEc2SessionWithProfile ProfileName: $'''default''' ProfileLocation: $'''example''' Ec2Client=> Ec2Client
```
入力: ProfileLocation:String ProfileName:String
出力: Ec2Client:Ec2ClientObject=>
ON ERROR可: CreateSessionFailed, InvalidProfileError, ProfileNotFoundError
固定: UseAccessKeys=False

## AWS.CreateSnapshot [A]
```
AWS.CreateSnapshot Ec2Client: Ec2Client VolumeId: $'''example''' Description: $'''example''' Name: $'''example''' Purpose: $'''example''' Snapshot=> Snapshot
```
入力: Description:String Name:String Purpose:String VolumeId:String Ec2Client:Ec2ClientObject
出力: Snapshot:Snapshot=>
ON ERROR可: AuthenticationFailureError, InvalidVolumeError, LimitExceededError, RequestFailedError, UnauthorizedOperationError

### AWS.CreateVolume のセレクター: CreateVolume, CreateVolumeFromSnapshot

## AWS.CreateVolume.CreateVolume [A]
```
AWS.CreateVolume.CreateVolume Ec2Client: Ec2Client AvailabilityZone: $'''example''' Size: $'''example''' Encrypted: False VolumeType: AWS.VolumeType.Gp2 Name: $'''example''' Purpose: $'''example''' Volume=> Volume
```
入力: AvailabilityZone:String Encrypted:Boolean Name:String Purpose:String Size:String VolumeType:VolumeType{Gp2,Standard,Io1,Sc1,St1} Ec2Client:Ec2ClientObject
出力: Volume:Volume=>
ON ERROR可: AuthenticationFailureError, InvalidParameterError, InvalidZoneError, LimitExceededError, NotAvailableInZoneError, RequestFailedError, UnauthorizedOperationError
固定: FromSnapshot=False

## AWS.CreateVolume.CreateVolumeFromSnapshot [A]
```
AWS.CreateVolume.CreateVolumeFromSnapshot SnapshotId: $'''example''' SnapshotSize: $'''example''' Ec2Client: Ec2Client VolumeType: AWS.VolumeType.Gp2 Encrypted: False AvailabilityZone: $'''example''' Purpose: $'''example''' Name: $'''example''' Volume=> Volume
```
入力: !SnapshotId:String SnapshotSize:String !Ec2Client:Ec2ClientObject !VolumeType:VolumeType{Gp2,Standard,Io1,Sc1,St1} !Encrypted:Boolean !AvailabilityZone:String Purpose:String Name:String
出力: Volume:Volume=>Volume
ON ERROR可: AuthenticationFailureError, InvalidParameterError, InvalidZoneError, LimitExceededError, NotAvailableInZoneError, RequestFailedError, UnauthorizedOperationError
固定: FromSnapshot=True

## AWS.DeleteSnapshot [A]
```
AWS.DeleteSnapshot Ec2Client: Ec2Client SnapshotId: $'''example'''
```
入力: SnapshotId:String Ec2Client:Ec2ClientObject
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, RequestFailedError, ResourceIsInUseError, UnauthorizedOperationError

## AWS.DeleteVolume [A]
```
AWS.DeleteVolume Ec2Client: Ec2Client VolumeId: $'''example'''
```
入力: VolumeId:String Ec2Client:Ec2ClientObject
ON ERROR可: AuthenticationFailureError, IncorrectStateError, InvalidParameterError, InvalidVolumeError, RequestFailedError, ResourceIsInUseError, UnauthorizedOperationError

## AWS.DescribeEC2Instance [A]
```
AWS.DescribeEC2Instance Ec2Client: Ec2Client InstanceState: AWS.InstanceState.All AvailabilityZone: $'''example''' InstanceIds: FileList Ec2Instances=> Ec2Instances
```
入力: AvailabilityZone:String InstanceIds:List InstanceState:InstanceState{Pending,All,Unknown,Running,ShuttingDown,Terminated,Stopping,Stopped} Ec2Client:Ec2ClientObject
出力: Ec2Instances:List=>
ON ERROR可: AuthenticationFailureError, InvalidInstanceIdError, RequestFailedError, UnauthorizedOperationError

### AWS.DescribeSnapshots のセレクター: DescribeAllSnapshots, DescribeSnapshotsByCustomFilter, DescribeSnapshotsById, DescribeSnapshotsByOwnerId, DescribeSnapshotsByRestorableUserId

## AWS.DescribeSnapshots.DescribeAllSnapshots [A]
```
AWS.DescribeSnapshots.DescribeAllSnapshots Ec2Client: Ec2Client Snapshots=> EBSSnapshots
```
入力: Ec2Client:Ec2ClientObject
出力: Snapshots:List=>
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, InvalidUserOrOwnerError, RequestFailedError, UnauthorizedOperationError
固定: DescribeSnapshotsMode=AllSnapshots

## AWS.DescribeSnapshots.DescribeSnapshotsByCustomFilter [A]
```
AWS.DescribeSnapshots.DescribeSnapshotsByCustomFilter SnapshotIds: List Ec2Client: Ec2Client RestorableByUserIds: List OwnerIds: List Snapshots=> EBSSnapshots
```
入力: !SnapshotIds:List<String> !Ec2Client:Ec2ClientObject !RestorableByUserIds:List<String> !OwnerIds:List<String>
出力: Snapshots:List<Snapshot>=>EBSSnapshots
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, InvalidUserOrOwnerError, RequestFailedError, UnauthorizedOperationError
固定: DescribeSnapshotsMode=SnapshotsByCustomFilter

## AWS.DescribeSnapshots.DescribeSnapshotsById [A]
```
AWS.DescribeSnapshots.DescribeSnapshotsById SnapshotIds: List Ec2Client: Ec2Client Snapshots=> EBSSnapshots
```
入力: !SnapshotIds:List<String> !Ec2Client:Ec2ClientObject
出力: Snapshots:List<Snapshot>=>EBSSnapshots
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, InvalidUserOrOwnerError, RequestFailedError, UnauthorizedOperationError
固定: DescribeSnapshotsMode=SnapshotsById

## AWS.DescribeSnapshots.DescribeSnapshotsByOwnerId [A]
```
AWS.DescribeSnapshots.DescribeSnapshotsByOwnerId Ec2Client: Ec2Client OwnerIds: List Snapshots=> EBSSnapshots
```
入力: !Ec2Client:Ec2ClientObject !OwnerIds:List<String>
出力: Snapshots:List<Snapshot>=>EBSSnapshots
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, InvalidUserOrOwnerError, RequestFailedError, UnauthorizedOperationError
固定: DescribeSnapshotsMode=SnapshotsByOwnerId

## AWS.DescribeSnapshots.DescribeSnapshotsByRestorableUserId [A]
```
AWS.DescribeSnapshots.DescribeSnapshotsByRestorableUserId Ec2Client: Ec2Client RestorableByUserIds: List Snapshots=> EBSSnapshots
```
入力: !Ec2Client:Ec2ClientObject !RestorableByUserIds:List<String>
出力: Snapshots:List<Snapshot>=>EBSSnapshots
ON ERROR可: AuthenticationFailureError, InvalidSnapshotError, InvalidUserOrOwnerError, RequestFailedError, UnauthorizedOperationError
固定: DescribeSnapshotsMode=SnapshotsByRestorableUserId

### AWS.DescribeVolumes のセレクター: DescribeAllVolumes, DescribeVolumesByIds, DescribeVolumesByInstance

## AWS.DescribeVolumes.DescribeAllVolumes [A]
```
AWS.DescribeVolumes.DescribeAllVolumes Ec2Client: Ec2Client Volumes=> EBSVolumes
```
入力: Ec2Client:Ec2ClientObject
出力: Volumes:List=>
ON ERROR可: AuthenticationFailureError, InvalidParameterError, RequestFailedError, UnauthorizedOperationError
固定: DescribeVolumesMode=AllVolumes

## AWS.DescribeVolumes.DescribeVolumesByIds [A]
```
AWS.DescribeVolumes.DescribeVolumesByIds VolumeIds: List Ec2Client: Ec2Client Volumes=> EBSVolumes
```
入力: !VolumeIds:List<String> !Ec2Client:Ec2ClientObject
出力: Volumes:List<Volume>=>EBSVolumes
ON ERROR可: AuthenticationFailureError, InvalidParameterError, RequestFailedError, UnauthorizedOperationError
固定: DescribeVolumesMode=SpecificVolumes

## AWS.DescribeVolumes.DescribeVolumesByInstance [A]
```
AWS.DescribeVolumes.DescribeVolumesByInstance Ec2Client: Ec2Client InstanceId: $'''example''' Volumes=> EBSVolumes
```
入力: !Ec2Client:Ec2ClientObject !InstanceId:String
出力: Volumes:List<Volume>=>EBSVolumes
ON ERROR可: AuthenticationFailureError, InvalidParameterError, RequestFailedError, UnauthorizedOperationError
固定: DescribeVolumesMode=AllVolumesOfTheSpecifiedInstance

## AWS.DetachVolume [A]
```
AWS.DetachVolume Ec2Client: Ec2Client VolumeId: $'''example''' Device: $'''example''' Force: False InstanceId: $'''example'''
```
入力: Device:String Force:Boolean InstanceId:String VolumeId:String Ec2Client:Ec2ClientObject
ON ERROR可: AuthenticationFailureError, IncorrectStateError, InvalidAttachmentError, InvalidParameterError, RequestFailedError, UnauthorizedOperationError, UnsupportedOperationError

## AWS.EndEC2Session [A]
```
AWS.EndEC2Session Ec2Client: Ec2Client
```
入力: Ec2Client:Ec2ClientObject
ON ERROR不可（BLOCK ... ON BLOCK ERROR で囲む）

## AWS.GetAvailableEC2Instances [A]
```
AWS.GetAvailableEC2Instances Ec2Client: Ec2Client InstanceState: AWS.InstanceState.All AvailabilityZone: $'''example''' Ec2InstancesInfo=> Ec2InstancesInfo
```
入力: AvailabilityZone:String InstanceState:InstanceState{Pending,All,Unknown,Running,ShuttingDown,Terminated,Stopping,Stopped} Ec2Client:Ec2ClientObject
出力: Ec2InstancesInfo:List=>
ON ERROR可: AuthenticationFailureError, RequestFailedError, UnauthorizedOperationError

## AWS.RebootEC2Instance [A]
```
AWS.RebootEC2Instance Ec2Client: Ec2Client InstanceIds: FileList
```
入力: InstanceIds:List Ec2Client:Ec2ClientObject
ON ERROR可: AuthenticationFailureError, IncorrectStateError, InvalidInstanceIdError, RequestFailedError, UnauthorizedOperationError, UnsupportedOperationError

## AWS.StartEC2Instance [A]
```
AWS.StartEC2Instance Ec2Client: Ec2Client InstanceIds: FileList StartingEc2Instances=> StartingEc2Instances
```
入力: InstanceIds:List Ec2Client:Ec2ClientObject
出力: StartingEc2Instances:List=>
ON ERROR可: AuthenticationFailureError, InsufficientCapacityError, InvalidInstanceIdError, RequestFailedError, UnauthorizedOperationError

## AWS.StopEC2Instance [A]
```
AWS.StopEC2Instance Ec2Client: Ec2Client InstanceIds: FileList Force: False Hibernate: False StoppingEc2Instances=> StoppingEc2Instances
```
入力: Force:Boolean Hibernate:Boolean InstanceIds:List Ec2Client:Ec2ClientObject
出力: StoppingEc2Instances:List=>
ON ERROR可: AuthenticationFailureError, InvalidInstanceIdError, RequestFailedError, UnauthorizedOperationError, UnsupportedOperationError
