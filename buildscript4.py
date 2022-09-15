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
import csv

#subprocess.call(['./setup.sh'])

#user = input("Enter a Github account: ")
#api_url = f'https://api.github.com/users/{user}/repos'

# username = 'cadenhong'

# repo_api_url = f'https://api.github.com/users/cadenhong/repos'
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

headers = ['name', 'description', 'language', 'html_url', 'created_at', 'updated_at']

with open('repo.json', 'r') as repo:
    r = json.load(repo)

dct = {}
lst = []

n = [ {'name': 'a', 'description': 'a', 'language': '', 'html_url': '', 'created_at': '', 'updated_at': ''},\
      {'name': 'b', 'description': 'b', 'language': '', 'html_url': '', 'created_at': '', 'updated_at': ''},\
      {'name': 'c', 'description': 'c', 'language': '', 'html_url': '', 'created_at': '', 'updated_at': ''},\
      {'name': 'd', 'description': 'd', 'language': '', 'html_url': '', 'created_at': '', 'updated_at': ''} ]

print(n[0]['name']) # a

# list of field values (i.e [name, desc, date, etc, etc, etc])
# dict(zip(header,list)) to create a dictionary, then append it to a list
# repeat for all the repos (12 total)

b = []
for repo in r:
    a = []
    for header in headers:
#        print(repo[header])
        #a = []
        a.append(repo[header])
    b.append(a)
print(b)
#    dictionary = dict(zip(headers,a))


# print(len(dictionary))

# # prints by header info 
# for header in headers:
#     for repository in r:
#         print(repository[header])

# for num in range(len(r)):
#     for header in headers:
#         dct[header] = r[num][header]
# print(len(r))

# with open('testing.txt', 'w') as t:
#     # prints all header by repo
#     for repos in r:
#         for h in headers:
#             t.write(repos[h])
        

# for num in range(len(r)):
#     for header in headers:
#         lst.append({header})
#         #dct[header] = r[num][header]
# print(len(lst))   
# #    print(dct)
# #print(len(dct))

# for num in range(len(r)):
#     for header in headers:
#         lst.append({header:r[num][header]})
#         # dct[header] = r[header]
#         # lst.append(dct)

# print(lst[0])

# print(len(lst))

# for num in range(len(r)):
#     for header in headers:
#         index = 0
#         info[header].append(r[num][header])
#         index += 1

# for num in range(len(r)):
#     for header in headers:
#         lst.append({header:r[header]})
#         print(lst)

# with open('{}.csv'.format(r[0]['owner']['login']), 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(info)

# new_json = []

# for i in range(len(r)):
#     for field in fields:
#         dict_pair = {}
#         dict_pair[field] = r[i][field]
#         new_json[i].append(dict_pair)
#         print(new_json)
#        new_json[i] = field
 #       new_json[field].append(r[i][field])

#print(new_json)