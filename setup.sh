#!/bin/bash

package=$(pip3 list | grep "requests")

if [ -z "$package" ] ; then
  echo $package "does not exist, installing now..."
  sudo apt update
  sudo apt upgrade -y
  pip3 install requests
  echo "Installation completed"
else
  echo $package "exists"
fi