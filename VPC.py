import boto3
ec2 = boto3.resource('ec2')

option = input("Here are some options: \n1.Create VPC\n2.Delete VPC \n)
while ("True"):
 #Create VPC
    if(option == "1"):
        #here all the info we will need for creating this vpc
        cidr_vpc = input('please set a CIDR for the VPC: (XXX.XXX.XXX.XXX/XX)')
        vpc_id = input('please set an Id for the vpc: ')
        igw_id = input("please set an id for the IGW: ")
        subnet_ip = input("please set an ip for this subnet: (XXX.XXX.XXX.XXX/XX)")
        subnet_id = input("please set an id for the subnet: ")
        group_name = input("Please set a security group name: ")
        group_des = input("Please write a small description: ")
        des_cidr_block = '0.0.0.0/0'
        cidr_ip = '0.0.0.0/0'
        protocol = input("which protocol do you want? (HTTP/HTTPS/SSH/ALL TCP etc...)")
        f_port = str(input("from which port you want to exit:"))
        t_port = str(input("from which port you want to enter:"))
        #vpc
        vpc = client.create_vpc(
        CidrBlock=cidr_vpc,
        vpcId=vpc_id)
        #igw and attach
        internetgateway = client.create_internet_gateway()
        vpc.attach_internet_gateway(
        InternetGatewayId=igw_id)
        #routetable and attach to subnet that you create
        routetable = vpc.create_route_table(
        VpcId=vpc_id)
        route = client.create_route_table(DestinationCidrBlock=des_cidr_block, GatewayId=igw_id)
        subnet = ec2.create_subnet(CidrBlock=subnet_ip, VpcId=vpc_id)
        routetable.associate_with_subnet(SubnetId=subnet_id)
        #security group permmison to all here we can make it what ever you want

        securitygroup = client.create_security_group(GroupName=group_name, Description=group_des,VpcId=vpc_id)
        securitygroup.authorize_ingress(CidrIp=cidr_ip, IpProtocol=protocol, FromPort=f_port, ToPort=t_port)

        #create an ec2
        choice = input("do you want to make an instance as well? y/n")
        if (choice == "yes" or choice == "y"):
            image_id = input("please insert and image id for the ec2: ")
            instance_type = input("please insert the type you want for the ec2: ")
            maxcount = str(input("How many instances do you wnat?: "))
            mincount = 1
            instances = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MaxCount=maxcount,
            MinCount=mincount,
            NetworkInterfaces=[{
                'SubnetId': subnet_id,
                'DeviceIndex': 0,
                'AssociatePublicIpAddress': True,
                'Groups': [securitygroup.group_id]
            }])
        else:
            break
#Delete VPC
    elif(option == "2"):
        #Terminate the EC2
        tagname = input("Please fill an instance name: ")
        tagvalue = input("Please fill a Value: ")
        gp_rm = input("what is the security group name you want to remove: ")
        rt_rm = input('what is the route table id?:')
        igw_rm = input("What is the igw id that you want to remove?: ")
        sub_rm = input("What is the subnet id that you want to remove?: ")
        vpc_rm = input("What is the vpc id that you want to remove?: ")

        ec2.instances.filter(Filters=[
        {'Name': 'tag': [tagname],'Values': [tagvalue]},
        {'Name': 'instance-state-name', 'Values': ['terminating']}
        ]).terminate()
        #Delete decurity group
        remove_gp = client.delete_security_group(
            GroupName =gp_rm,
        )
        #Delete routetable
        rm_rtb = client.delete_route_table(
            RouteTableId=rt_rm,
        )
        #Delete igw
        rm_igw = client.delete_internet_gateway(
            InternetGatewayId=igw_rm,
        )
        #Delete subnets
        rm_sub = client.delete_subnet(
            SubnetId=sub_rm,
        )
        #Delete vpc
        rm_vpc = client.delete_vpc(
            VpcId=vpc_rm,
        )
    else:
        print("Only numbers between 1-3")
