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
#	- 
#	- 
#	- 
#
##################################################################################

import subprocess
import requests

#subprocess.call(['./setup.sh'])

user = input("Enter a Github account to check: ")
api_url = f'https://api.github.com/users/{user}/repos'
response = requests.get(api_url)
print(response.json())

# sections = ['arts', 'automobiles', 'books', 'business', 'fashion', 'food', 'health', 'home', 'insider', 'magazine', 'movies', 'nyregion', 'obituaries', 'opinion', 'politics', 'realestate', 'science', 'sports', 'sundayreview', 'technology', 'theater', 't-magazine', 'travel', 'upshot', 'us', 'world']
# for section in sections:
#     print(f'{section}', end='|')