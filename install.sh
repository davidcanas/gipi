if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
mv gip.py gip
chmod +x gip
cp gip /usr/bin/


echo "GIP installed use gip version to verify!"