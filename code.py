#Project : Information Gathering tool

import sys #Library to handle command-line arguments
import requests #Library to make HTTP requests
import socket #Library to handle network-related tasks
import json #Library to handle JSON data

#Check if URl is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

#Fetch headers of the provided website
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#Resolve the domain name to an IP address
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe Ip address of "+sys.argv[1]+" is: "+gethostby_ + "\n")

#Fetch location and other details using the ipinfo.io API
req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

#print the retrieved information
print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
print("Organization: "+resp_["org"])