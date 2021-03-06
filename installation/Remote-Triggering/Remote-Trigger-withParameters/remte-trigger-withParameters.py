# Import libraries
from urllib import response
import requests
import os
import json

try:
    # Read the configuration file
    full_path = os.path.realpath(__file__)  ### Get the path of current working directory
    cwd = os.path.dirname(full_path)        ### Get the path of current working directory
    print(f"[Info]: Current working directory is : {cwd}")
    # Read the config.json 
    configFile = open(cwd+ "/config.json", "r")
    configContent = configFile.read()

    print(type(configContent))  

    jsonConfigContent = json.loads(configContent)  ### converting string to json format

    # Parse the configuration file
    jenkins_url = jsonConfigContent['jenkins_url']
    user = jsonConfigContent['user']
    user_token = jsonConfigContent['user_token']
    job_name = jsonConfigContent['job_name']
    job_token = jsonConfigContent['job_token']

except Exception as e:
    print(f"[Error]: In using the configuration file: {e}")

# Send the POST request and check the status
#url = jenkins_url+'/job/'+job_name+'/build?token='+job_token
#print(f"[Info]: Triggering the job (url)")

url = jenkins_url+'/job/'+job_name+'/buildWithParameters?token='+job_token

my_data = {
    "IMAGE_NAME" : "python-app",
    "IMAGE_TAG": "2.22",
    "ENVIRONMENT": "dev",
    "isWorking": False
}

response = requests.post(url, auth=(user, user_token), data=my_data)

if int(response.status_code) != 201:
    print(f"[Error]: Triggering job failed with status {response.status_code}")
    exit(1)
print(f"[Success]: Triggering job is successful with status code {response.status_code}")