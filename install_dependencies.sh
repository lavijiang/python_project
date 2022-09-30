#!/bin/bash

install_list=("rest_framework")
for variable in $install_list  
do  
echo "begin install $variable"
pip3 install $variable
echo "finish install $variable"
done

