import boto3

ec2 = boto3.resource('ec2')
while("True"):
    choice = input("Here are some options: \n1.Describe your instances \n2.Deploy your instances \n3.Destroy your instances \n4.Stop your instances \n5.Start your instances\n")
#Describe an instance
    if (choice == "1"):
        client = boto3.client('ec2')
        response = client.describe_instances()
        for x in response['Reservations']:
            for y in x['Instances']:
                print("ID: " + y['InstanceId'] + "\nIP Address: " + y['PublicIpAddress'])
# create a new EC2 instance
    elif (choice == "2"):
        instances = ec2.create_instances(
            ImageId=input("Pleae fill an ImageId: "),
            MinCount=1,
            MaxCount=int(input("enter how many instances do you want:\n")),
            InstanceType=input("Pleae fill the Instace type you want: "),
            KeyName=input("Pleae fill a KeyName: ")
        )
#Kill an instance
    elif (choice == "3"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['terminating']}
        ]).terminate()

#Stop an instance
    elif (choice == "4"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]).stop()

#Start an instnace
    elif (choice == "5"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]).start()
        
    exit= input("Do you want something else? y/n")
    if(exit == "y" or exit == "yes")
        break
    else:
        continue
              
print("Were done!")
