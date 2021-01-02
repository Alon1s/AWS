import boto3
from datetime import *
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError 
from datetime import *
import yaml
from statsd import *
import json

arns = []

client = boto3.client('acm')
response = client.list_certificates()
get_file = open('the path to the file', 'r')
file = get_file.read()
dictionary = yaml.load(file, Loader=yaml.FullLoader)
server_name = dictionary['server']
port_number= dictionary['port']
statsd_client = StatsClient(server_name, port_number)

for x in response['CertificateSummaryList']:
    arn_cert = x['CertificateArn']
    arns.append(arn_cert)
for arn in arns:
    new = client.describe_certificate(
    CertificateArn=arn
    )
    alon=str(new['Certificate']['NotAfter'])
    domain_name = new['Certificate']['DomainValidationOptions'][0]['DomainName']
    clean_date = alon[0:19]
    obj = datetime.strptime(clean_date, '%Y-%m-%d %H:%M:%S').date()
    delta = (obj - date.today()).days
    if delta <= 0:
        pass
    else:
        if domain_name[0] == '*':
            new_name=domain_name[2:]
            statsd_client.gauge(f'what_ever_you_chose.exp', delta)
        else:
            statsd_client.gauge(f'what_ever_you_chose.exp', delta)
