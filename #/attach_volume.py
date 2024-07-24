import boto3

# Initialize the EC2 client using Boto3
ec2_client = boto3.client('ec2')

# Replace these variables with your specific details
volume_id = 'vol-0379ff38a1492121f'  # Your EBS volume ID
instance_id = 'i-08fb273abf2019ecb'  # Your EC2 instance ID
device_name = '/dev/sdg'  # The device name to expose to the instance (e.g., /dev/sdf, /dev/xvdf)

# Attach the volume to the instance
try:
    response = ec2_client.attach_volume(
        VolumeId=volume_id,
        InstanceId=instance_id,
        Device=device_name
    )
    print(f'Successfully attached volume {volume_id} to instance {instance_id} as {device_name}')
except Exception as e:
    print(f'Error attaching volume: {e}')
