"""
To add a user to a GitHub organization programmatically
"""

import requests
import json

# Constants
github_api_url = 'https://api.github.com'
access_token = 'YOUR_ACCESS_TOKEN'  # Replace with your personal access token
organization = 'YOUR_ORGANIZATION'  # Replace with your organization name
username = 'USERNAME_TO_ADD'  # Replace with the username to add


# API call to add a user to the organization
def add_user_to_organization():
    url = f'{github_api_url}/orgs/{organization}/memberships/{username}'
    headers = {'Authorization': f'Token {access_token}'}
    data = {'role': 'member'}  # Specify the role as 'member' or 'admin' as desired
    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response.status_code


# Main script
try:
    status_code = add_user_to_organization()
    if status_code == 200:
        print(f"User '{username}' added to the organization '{organization}' successfully.")
    else:
        print(f"Failed to add user '{username}' to the organization '{organization}'. Status code: {status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
