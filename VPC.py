import boto3
ec2 = boto3.resource('ec2')

option = input("Here are some options: \n1.Create VPC\n2.Delete VPC \n3.Describe VPC")
while ("True"):
 #Create VPC
    if(option == "1"):
        #vpc
        cidr_vpc = input('please set a CIDR for the VPC: (XXX.XXX.XXX.XXX/XX)')
        vpc_id =input('please set an Id for the vpc: ')
        vpc = client.create_vpc(
        CidrBlock=cidr_vpc,
        vpcId=vpc_id)
        #igw and attach
        igw_id = input("please set an id for the IGW: ")
        internetgateway = client.create_internet_gateway()
        vpc.attach_internet_gateway(
        InternetGatewayId=igw_id)
        #routetable and attach to subnet that you create
        routetable = vpc.create_route_table(
        VpcId=vpc_id)
        route = client.create_route_table(DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
        subnet = ec2.create_subnet(CidrBlock=input("Give an Ip for the VPC:XXX.XXX.XXX.XXX/XX"), VpcId=vpc_id)
        subnet_id = input("please set an id for the subnet: ")
        routetable.associate_with_subnet(SubnetId=subnet_id)
        #security group permmison to all here we can make it what ever you want
        group_name = input("Please set a group name: ")
        securitygroup = client.create_security_group(GroupName=group_name, Description=input("Please write a small description: "),VpcId=vpc_id)
        securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='TCP', FromPort=80, ToPort=80)

        #create an ec2
        instances = ec2.create_instances(
            ImageId='ami-0de53d8956e8dcf80',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            NetworkInterfaces=[{
                'SubnetId': subnet_id,
                'DeviceIndex': 0,
                'AssociatePublicIpAddress': True,
                'Groups': [securitygroup.group_id]
            }])
#Delete VPC
    elif(option == "2"):
        #Terminate the EC2
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        ec2.instances.filter(Filters=[
        {'Name': 'tag': [tagname],'Values': [tagvalue]},
        {'Name': 'instance-state-name', 'Values': ['terminating']}
        ]).terminate()
        #Delete decurity group
        rm_gp = client.delete_security_group(
            GroupName =group_name,
        )
        #Delete routetable
        rm_rtb = client.delete_route_table(
            RouteTableId=input('what is the route table id?:'),
        )
        #Delete igw
        rm_igw = client.delete_internet_gateway(
            InternetGatewayId=igw_id,
        )
        #Delete subnets
        rm_sub = client.delete_subnet(
            SubnetId=subnet_id,
        )
        #Delete vpc
        rm_vpc = client.delete_vpc(
            VpcId=vpc_id,
        )
#Describe the VPC
    elif (option == "3"):
        #The vpc
        des_vpc = client.describe_vpcs(
            VpcIds=['Here the id']
            ,
        )
        #The IGW
        response = client.describe_internet_gateways(
            Filters=[
                {
                    'Name': #here the name,
                    'Values': [
                        #####,
                    ],
                },
            ],

    else:
        print("Only numbers between 1-3")
