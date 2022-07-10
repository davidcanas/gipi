if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
pip install -r requirements.txt
cp gipi.py gipi
chmod +x gipi
cp gipi /usr/bin/
dos2unix /usr/bin/gipi

echo "GIPI installed with success! Use gipi help to see all commands!"