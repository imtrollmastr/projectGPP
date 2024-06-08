import json
import requests
import sys
import getpass
def getLocationData():
    ip = input("Enter IP Address: ")
    # Make request to https://ipinfo.io/
    url = "https://ipinfo.io/"+ ip +"/json"
    print("Requesting geolocation data...")
    import requests
    request = requests.get(url)
    print("Decoding information...")
    decode = json.loads(request.text)
    # Decoded information
    print("Decoding variables...")
    ip = decode["ip"]
    city = decode["city"]
    region = decode["region"]
    country = decode["country"]
    loc = decode["loc"]
    org = decode["org"]
    try:
        postal = decode["postal"]
        timezone = decode["timezone"]
        # Print decoded information
        print("Successfully processed information.")
        print("IP Address: " + ip)
        print("City: " + city)
        print("Region: " + region)
        print("Country: " + country)
        print("Latitude and Longitude: " + loc)
        print("Organization: " + org)
        print("Postal Code: " + postal)
        print("Timezone: " + timezone)
        getLocationData()
    except:
        timezone = decode["timezone"]
        # Print decoded information
        print("Successfully processed information.")
        print("IP Address: " + ip)
        print("City: " + city)
        print("Region: " + region)
        print("Country: " + country)
        print("Latitude and Longitude: " + loc)
        print("Organization: " + org)
        print("Timezone: " + timezone)
        getLocationData()

sys.stdout.write("\x1b]2;Geolocation Private Processer \x07")
clienturl = "https://api.ipify.org?format=json"
clientrequest = requests.get(clienturl)
clientdecode = json.loads(clientrequest.text)
clientaddress = clientdecode["ip"]
print("Successfully loaded GP+ from "+clientaddress+".")
path = "/Users/"+getpass.getuser()+"/Desktop/important/projects/gpp/verifiedaddress.json"
verifiedfile = open(path, "r")
content = verifiedfile.read()
decodedcontent = json.loads(content)
if clientaddress == decodedcontent["gppHolderID"]:
    print("Successfully identified user.")
    getLocationData()
else:
    print("Unable to verify client source.")
