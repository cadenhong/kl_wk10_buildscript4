#!/bin/bash

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