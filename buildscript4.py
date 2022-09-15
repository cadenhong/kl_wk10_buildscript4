############################################################################################
#
# Name: Caden Hong
#
# Date: September 15, 2022
#
# Description: Send a GET request to GitHub's API, retrieve and organize data into a CSV:
#	- try:
#       - Import the following packages: subprocess, json, csv, time, getpass, requests
#	- except (import error):
#       - Run the setup.sh script to install requests package
#       - Import the following packages: subprocess, json, csv, time, getpass, requests
#	- finally:
#       - Prompt user to enter a GitHub account to look up, store in username variable
#       - Prompt user to enter their GitHub token to use for API call, store in token variable
#       - Set repo_api_url using the entered username
#       - try:
#           - Send a GET request using repo_api_url, username, and token, store in response
#           - Raise error if one occurs
#       - except (HTTP error):
#           - Inform that there was an invalid HTTP response
#       - except (connection error):
#           - Inform that there was a network problem
#       - except (redirect error):
#           - Inform that user exceeded redirection limits
#       - except (other errors):
#           - Inform user of the error's status code
#       - else (to run if no exception is raised):
#           - Print the status code to confirm successful GET request
#           - Store the GET response as a JSON in response_json variable
#           - Store content of response_json in a username_repos.json file
#           - Store the specific key value to extract in a list called headers
#           - Open the JSON file and store in user_repos variable
#           - Create an empty list called csv_rows
#           - For each repo in user_repos:
#               - Create an empty list called csv_row
#               - For each header in headers:
#                   - Append the corresponding info found in repo to csv_row
#               - Append contents of csv_row into csv_rows
#           - Use csv.writer() method to store the headers and csv_rows in username_repos.csv
#       - finally:
#           - Close the Request object (response variable)
#
# Potential Issues:
#	- Without GitHub token provided, there is a limit on how many requests one can make
#	- If GitHub token is entered, it will be saved as a variable - potential security issue?
#	- Script is quite long, could potentially utilize modules and functions to shorten
#
############################################################################################

try:
    import subprocess, json, csv, time, getpass, requests
except ImportError:
    subprocess.call(['./setup.sh'])
    import subprocess, json, csv, time, getpass, requests
finally:
    print("============================================================================================")
    print("KURA LABS - BUILD SCRIPT 4".center(92))
    print("============================================================================================")
    time.sleep(1)
    print("Send a GET request to the GitHub API to retrieve a complete list of a user's public repos, ")
    print("store it in user_repos.json, then extract specific data to store in user_repos.csv.")
    time.sleep(3)
    print()
    print("To proceed, provide a valid GitHub username and your GitHub token to access the API.")
    print()
    print("You may run this script without a token (leave blank), but it will limit the number ")
    print("of requests that can be sent per hour.")
    print()
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

        print("\nBoth files have been generated!")
        time.sleep(1)
    finally:
        print()
        print("Closing API connection...")
        time.sleep(1)
        response.close()
        print("============================================================================================")