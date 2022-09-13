#!/bin/bash

package=$(pip3 list | grep "requests")

if [ -z "$package" ] ; then
  echo "Package does not exist"
  sudo apt update
  sudo apt upgrade -y
  pip3 install requests
else
  echo $package "EXISTS"
fi