#################################################################################
#
# Name: Caden Hong
#
# Date: September 12, 2022
#
# Description: This script :
#	- 
#	- 
#	- 
#	- 
#
# Potential Issues:
#	- Without Github token provided, there is a limitation on how many calls you can make to the API per hour
#	- 
#	- 
#
##################################################################################

import subprocess
import requests
import json

#subprocess.call(['./setup.sh'])

#user = input("Enter a Github account: ")
#api_url = f'https://api.github.com/users/{user}/repos'

# username = 'cadenhong'
# user_api_url = f'https://api.github.com/users/cadenhong'
# repo_api_url = f'https://api.github.com/users/cadenhong/repos'
# user_response = requests.get(user_api_url, auth=(username,token)).json()
# repo_response = requests.get(repo_api_url, auth=(username,token)).json()

# print(user_response['name'])
# print(repo_response[0]['name'])
# print(repo_response[0]['html_url'])
# print(repo_response[0]['description'])
# print(repo_response[0]['created_at'])
# print(repo_response[0]['updated_at'])
# print(repo_response[0]['language'])

# with open('user.json', 'w') as user:
#     json.dump(user_response, user, indent=2)

# with open('repo.json', 'w') as repo:
#     json.dump(repo_response, repo, indent=2)


# ------------------------ working with json files -------------------------------

info = {'name': [], 'description': [], 'language': [], 'html_url': [], 'created_at': [], 'updated_at': []}
headers = list(info.keys())
print(headers)

with open('user.json', 'r') as user:
    u = json.load(user)

with open('repo.json', 'r') as repo:
    r = json.load(repo)

print(r[0]['owner']['login'])

for repo in range(len(r)):
    for header in range(len(headers)):
        print(r[repo][headers[header]], end=", ")
    print()