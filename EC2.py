import boto3

ec2 = boto3.resource('ec2')
while("True"):
    option = input("Here are some options:\n1.create an instances \n2.Start your instances \n3.Stop your instances \n4.Terminate your instances\n")
# create a new EC2 instance
    if (option == "1"):
        instances = ec2.create_instances(
            ImageId=input("Pleae fill an ImageId: "),
            MinCount=1,
            MaxCount=int(input("enter how many instances do you want:\n")),
            InstanceType=input("Pleae fill the Instace type you want: "),
            KeyName=input("Pleae fill a KeyName: ")
        )
        break
#Start 
    elif (option == "2"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]).start()
        break
#Stop
    elif (option == "3"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]).stop()
        break
#Terminate 
    elif (option == "4"):
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
            {'Name': 'tag': [tagname], 'Values': [tagvalue]},
            {'Name': 'instance-state-name', 'Values': ['terminating']}
        ]).terminate()
        break
    else:
        print("Only numbers between 1-4")
