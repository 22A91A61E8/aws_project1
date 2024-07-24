#/create_volume.py
import boto3

# Set up Boto3 client for EC2
ec2_client = boto3.client('ec2')

# Parameters for the new volume
availability_zone = 'us-east-1c'  # Change to your desired availability zone
volume_size = 5 # Size in GiB
volume_type = 'gp2'  # General Purpose SSD

# Create the volume
response = ec2_client.create_volume(
    AvailabilityZone=availability_zone,
    Size=volume_size,
    VolumeType=volume_type
)

# Get the volume ID from the response
volume_id = response['VolumeId']
print(f'Created volume with ID: {volume_id}')

# Wait until the volume is available
waiter = ec2_client.get_waiter('volume_available')
waiter.wait(VolumeIds=[volume_id])

# Instance ID to which the volume will be attached
instance_id = 'i-08fb273abf2019ecb'  # Replace with your instance ID

# Device name for the volume attachment
device_name = '/dev/sdh'  # Ensure this is an available device name on your instance

# Attach the volume to the instance
response = ec2_client.attach_volume(
    VolumeId=volume_id,
    InstanceId=instance_id,
    Device=device_name
)

print(f'Attached volume {volume_id} to instance {instance_id} as {device_name}')
