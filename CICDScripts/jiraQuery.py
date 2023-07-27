import requests
import base64
import json
import sys  # Used to read command line arguments

#This tool will pull 
email = sys.argv[1]  # Use the first command line argument as the email
api_token = sys.argv[2]  # Use the second command line argument as the API token
domain = sys.argv[3]  # Use the third command line argument as the domain
jql = sys.argv[4]  # Use the fourth command line argument as the JQL query

headers = {
    'Authorization': f'Basic {base64.b64encode(f"{email}:{api_token}".encode()).decode()}',
    'Accept': 'application/json',
}

response = requests.get(
    f'https://{domain}.atlassian.net/rest/api/3/search?jql={jql}&expand=renderedFields',
    headers=headers
)

data = response.json()

# Save the data to a file
with open('issue_data.json', 'w') as file:
    json.dump(data, file, indent=4)
