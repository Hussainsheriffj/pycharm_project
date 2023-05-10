import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-1")


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'dev']   # if you need only dev snapshot 'Values': ['dev']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)

# we are scheduling the backup everyday, 5 seconds for testing
schedule.every(5).seconds.do(create_volume_snapshots)
while True:
    schedule.run_pending()

# print(volumes['Volumes'])