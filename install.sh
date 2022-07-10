if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
pip install -r requirements.txt
cp gipi.py gipi
chmod +x gipi
cp gipi /usr/bin/
find . -type f -print0 | xargs -0 dos2unix

echo "GIPI installed with success! Use gipi help to see all commands!"