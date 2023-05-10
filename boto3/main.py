import boto3

# ec2_client = boto3.client('ec2') this will take the default region from aws config.
# If want to check from other region check below
ec2_client = boto3.client('ec2', region_name="us-east-2")
ec2_resource = boto3.resource('ec2', region_name="us-east-2")

new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        },
    ]
)

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])








import requests
import smtplib       # using this module to send email
import os            # to use email id and password as env variable

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# we are repeating the email feature, so creating a function


def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()  # for secure encrypted line
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


try:
    response = requests.get('http://ec2-54-67-109-240.us-west-1.compute.amazonaws.com:8080/')
    if response.status_code == 200:
        print('Application is running successfully')
    else:
        print('Application down, please fix it')
    # print(response.status_code)
        # to send an email we need a sender email and a receiver email
        # google it for different email provider 587 is the gmail port
        msg = f"Application returned {response.status_code}"
        send_notification(msg)
except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)



