#!/bin/bash

############################################################################################
#
# Name: Caden Hong
#
# Date: September 15, 2022
#
# Description: Check user's environment to see if they have the requests package installed:
#   - Check modules using "pip3 list" and grep "requests", store in package variable
#   - If the package variable is not empty:
#       - sudo apt update
#       - sudo apt upgrade -y
#       - pip3 install requests
#   - Else:
#	      - Notify user that package exists
#
# Potential Issues:
#	- User may not have pip3 installed, they may still run pip
#	- This script works for requests package, but would benefit if package can be specified
#
############################################################################################

echo "============================================================================================"
echo "Checking environment for necessary package to run this script..."
sleep 2

package=$(pip3 list | grep "requests")

if [ -z "$package" ] ; then
  echo "requests package does not exist, installing now..."
  sudo apt update
  sudo apt upgrade -y
  pip3 install requests
else
  echo $package "exists"
fi