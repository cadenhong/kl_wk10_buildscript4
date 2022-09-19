# kl_wk10_buildscript4
Using both Python and Bash, interact with an API to gather data and organize the retrieved data into a CSV format. The API used in this script is [GitHub API](https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api).

## Tasks
1. Connect to an API and retrieve data using a GET request
2. Create a CSV file of the data retrieved
3. Only 6 columns are required (e.g. of the MLB API: Player’s name, number, team, position, height and weight)
4. The script can be interactive or not interactive
5. CSV file must be formatted properly

## Files and Folders
- [buildscript4.py](https://github.com/cadenhong/kl_wk10_buildscript4/blob/main/buildscript4.py): Main Python script - used to send GET request to GitHub's API, retrieve data, and generate a CSV file of select columns
  - Modules used: `subprocess`, `json`, `csv`, `time`, `getpass`, `requests`
- [cadenhong_repos.csv](https://github.com/cadenhong/kl_wk10_buildscript4/blob/main/cadenhong_repos.csv): CSV file generated after running the script using my GitHub account as user input
- [instructions.txt](https://github.com/cadenhong/kl_wk10_buildscript4/blob/main/instructions.txt): Instructions provided by KL
- [setup.sh](https://github.com/cadenhong/kl_wk10_buildscript4/blob/main/setup.sh): Script to check for and install `requests` package required to run
