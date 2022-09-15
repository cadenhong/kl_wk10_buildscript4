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

import subprocess, requests, json, csv, time, getpass

print("============================================================================================")
print("KURA LABS - BUILD SCRIPT 4".center(92))
print("============================================================================================")
time.sleep(1)
print("Send a GET request to the GitHub API to retrieve a complete list of a user's public repos, ")
print("store it in user_repos.json, then extract specific data to store in user_repos.csv.")
time.sleep(3)
print()
print("Checking environment for necessary package to run this script...")
time.sleep(2)
subprocess.call(['./setup.sh'])
time.sleep(1)
print()
print("To proceed, provide a valid GitHub username and your GitHub token to access the API.")
print()
print("You may run this script without a token (leave blank), but it will limit the number ")
print("of requests that can be sent per hour.")
print("--------------------------------------------------------------------------------------------")
time.sleep(4)
username = input("Enter a GitHub account: ")
token = getpass.getpass("Enter your GitHub token (press enter to skip): ")
repo_api_url = f'https://api.github.com/users/{username}/repos'

try:
    response = requests.get(repo_api_url, auth=(username,token))
    time.sleep(1)
    response.raise_for_status()
    print()
except requests.exceptions.HTTPError as http_err:
    print(f'ERROR! Invalid HTTP Response:\n{http_err}')
except requests.exceptions.ConnectionError as network_err:
    print(f'ERROR! Network Problem:\n{network_err}')
except requests.exceptions.TooManyRedirects as limit_err:
    print(f'ERROR! Exceeding Redirection Limit:\n{limit_err}')
except requests.exceptions.RequestException as other_err:
    print(f'ERROR!\n{requests.status_codes}')
else:
    print(f'GET request successful, response code: {response.status_code}')
    time.sleep(1)
    print(f'\nGenerating {username}_repos.json...')
    time.sleep(2)

    response_json = response.json()
    with open(f'{username}_repos.json', 'w') as repo:
        json.dump(response_json, repo, indent=2)

    headers = ['name', 'description', 'language', 'created_at', 'updated_at', 'html_url']
    
    with open(f'{username}_repos.json', 'r') as repo:
        user_repos = json.load(repo)

    csv_rows = []
    for repo in user_repos:
        csv_row = []
        for header in headers:
            csv_row.append(repo[header])
        csv_rows.append(csv_row)

    print(f'Generating {username}_repos.csv...')
    time.sleep(2)

    with open(f'{username}_repos.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(csv_rows)
    
    print("\nBoth files have been generated")
    time.sleep(1)
finally:
    print("--------------------------------------------------------------------------------------------")
    print("Closing API connection...")
    time.sleep(1)
    response.close()
    print("============================================================================================")