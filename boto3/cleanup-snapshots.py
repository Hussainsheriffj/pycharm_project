import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="us-west-1")

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']   # if you need only dev snapshot 'Values': ['dev']
        }
    ]
)

for volume in volumes['Volumes']:
    self_snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]  # if you need only dev snapshot 'Values': ['dev']
            }
        ]
    )
    sorted_by_date = sorted(self_snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    for snap in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)


# # snapshots created by us not by aws
# self_snapshots = ec2_client.describe_snapshots(
#     OwnerIds=['self']
# )
# sorted_by_date = sorted(self_snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
#
#
# # view snapshots after from 3
# for snap  in sorted_by_date[2:]:
#     print(snap['SnapshotId'])
#     print(snap['StartTime'])
#
# # deleting the snapshot
# for snap  in sorted_by_date[2:]:
#     response = ec2_client.delete_snapshot(
#     SnapshotId=snap['SnapshotId']
#     )
#     print(response)





# printing the startTime of all snapshots and sorted desc snapshots
# for snap in self_snapshots['Snapshots']:
#     print(snap['StartTime'])
#
# print('################')
#
# for snap in sorted_by_date:
#     print(snap['StartTime'])
# print(self_snapshots['Snapshots'])

