#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
echo "1/4 downloading the dependencies (requests/tracecolor)"
pip install -r requirements.txt
echo "2/4 Copying gipi.py file to gipi file"
cp gipi.py gipi
echo "3/4 Making the file executable" 
chmod +x gipi
echo "4/4 Moving gipi file to /usr/bin"
cp gipi /usr/bin/

echo "GIPI installed with success! Use gipi help to see all commands!"
