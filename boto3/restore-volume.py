# here we are typing to attach latest snapshot as volume to the ec2 instance
import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="us-west-1")
ec2_resource = boto3.resource('ec2', region_name="us-west-1")

instance_id = "i-093ff30a79f9144ab"

# finding volume attached to the above instance id
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]
# print(instance_volume)

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(latest_snapshot['StartTime'])

# creating a volume from the latest snapshot
new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="us-west-1c",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)
# new volume takes time to create to attach it to the ec2 instance
# below we are checking whether the volume is ready or not if ready then attaching it to the instance
while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='/dev/xvdb'  # changing from xvda to xvda same name is not acceptable
        )
        break   # breaking the loop from repeating after attaching the volume

# we have attached this code inside the above while loop
# ec2_resource.Instance(instance_id).attach_volume(
#     VolumeId=new_volume['VolumeId'],
#     Device='/dev/xvdb'   # changing from xvda to xvda same name is not acceptable
# )
