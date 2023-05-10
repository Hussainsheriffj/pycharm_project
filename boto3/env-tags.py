import boto3

ec2_client_cali = boto3.client('ec2', region_name="us-west-1")
ec2_resource_cali = boto3.resource('ec2', region_name="us-west-1")

ec2_client_ohio = boto3.client('ec2', region_name="us-east-2")
ec2_resource_ohio = boto3.resource('ec2', region_name="us-east-2")

instance_id_cali = []
instance_id_ohio = []

reservations_cali = ec2_client_cali.describe_instances()['Reservations']
for reservation in reservations_cali:
    instances = reservation['Instances']
    for instance in instances:
        instance_id_cali.append(instance['InstanceId'])

response = ec2_resource_cali.create_tags(
    Resources=instance_id_cali,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
for reservation in reservations_ohio:
    instances = reservation['Instances']
    for instance in instances:
        instance_id_ohio.append(instance['InstanceId'])

response = ec2_resource_ohio.create_tags(
    Resources=instance_id_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)