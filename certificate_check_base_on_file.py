from datetime import *
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
import yaml
from statsd import *

#in this specific script its a service which run on container, you can put your file when that you want
get_file = open('your_path', 'r')
file = get_file.read()
dictionary = yaml.load(file, Loader=yaml.FullLoader)
urls_prod = dictionary['domain']['prod']
urls_prep = dictionary['domain']['prep']
server_name = dictionary['server']
port_number= dictionary['port']


statsd_client = StatsClient(server_name, port_number)

for url in urls_prod:
    base_url = url
    port = '443'

    hostname = base_url
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = ssock.getpeercert()
   
        x = data['notAfter']
        obj = datetime.strptime(x, '%b %d %H:%M:%S %Y GMT').date()
        delta = (obj - date.today()).days

    statsd_client.gauge(f'whatever_you_want.exp', delta)

for url in urls_prep:
    base_url = url
    port = '443'

    hostname = base_url
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = ssock.getpeercert()

        x = data['notAfter']
        obj = datetime.strptime(x, '%b %d %H:%M:%S %Y GMT').date()
        delta = (obj - date.today()).days   
        
    statsd_client.gauge(f'what_ever_you_want.exp', delta)  
