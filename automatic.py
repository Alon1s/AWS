#!/bin/python3

import boto3
from time import sleep

def deploy_instance():
    ec2 = boto3.resources('ec2')
    instances = ec2.create_instances(
         ImageId=input("Enter ami ID:\n"),
         MinCount=1,
         MaxCount=int(input("How many instances you want?\n")),
         InstanceType=input(Which type of instance you want?\n),
         KeyName=input("What name you want for the key to access the server?\n") 
)
def describe_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for x in response['Reservations']:
        for y in x['Instances']:
            print("ID: " + y['InstanceId'] + "\nIP Address: " + x['PrivateIpAddress'])
            ##### there are many things that we can add to describe the instance see more from boto3 documation ####
def destroy_instance():
    instances=input("Enter the ids of the instances that you want to destroy: ")
    ids = [instances]
    ec2 = boto3.resources('ec2')
    
    ec2.instances.filter(InstancesIds = ids).terminate()
    
def stop_instance():
    instances=input("Enter the ids of the instances that you want to destroy: ")
    ids = [instances]
    ec2 = boto3.resources('ec2')
    
    ec2.instances.filter(InstancesIds = ids).stop()
    
def start_instance():
    instances=input("Enter the ids of the instances that you want to destroy: ")
    ids = [instances]
    ec2 = boto3.resources('ec2')
    
    ec2.instances.filter(InstancesIds = ids).start()
    
def menu():
    while(True):
        choice=input("Menu:\n1.Describe EC2 \n2.Deploy EC2 \n3.Destroy EC2 \n4.Stop EC2 \n5.Start EC2")
        if(choice=="1"):
            print("Here is the IP and ID of the instance: ")
            sleep(1)
            describe_instance()
        elif(choice=="2")
            deploy_instance()
        elif(choice=="3")
            destroy_instance()
        elif(choice=="4")
            stop_instance()    
        elif(choice=="5")
            start_instance()
        else:
            print("Please pick a number from 1-5...")
            continue
        exit=input("Do you want something else? yes/no\n")
        if(exit=="yes"):
            print("Were done.\n")
            break

            
##### from here thre script will start ####
main()
