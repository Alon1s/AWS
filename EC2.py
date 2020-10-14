import boto3

choice = input("enter  your  choice: \n1.describe your instances \n2.deploy your instances \n3.destroy your instances \n4.stop your instances \n5.start your instances")
#Describe an instance
if choice == "1":
    client = boto3.client('ec2')
    response = client.describe_instances()
    for x in response['Reservations']:
        for y in x['Instances']:
            print("ID: " + y['InstanceId'] + "\nIP Address: " + y['PublicIpAddress'] + "\n---------------------------------------")
# create a new EC2 instance
elif choice == "2":
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId='ami-0bbe28eb2173f6167',
        MinCount=1,
        MaxCount=int(input("enter how many instances do you want:\n")),
        InstanceType='t2.micro',
        KeyName='Alon_Sharf'
    )
#Kill an instance
elif choice == "3":
    instances = input("enter the ids of the instances that you want to stop:")
    ids = [instances]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=ids).terminate()


#Stop an instance
elif choice == "4":
    instances = input("enter the ids of the instance that you want to stop:")
    ids = [instances]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=ids).stop()

#Start an instnace
elif choice == "5":
    instances = input("enter the ids of the instance that you want to start:")
    ids = [instances]
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=ids)