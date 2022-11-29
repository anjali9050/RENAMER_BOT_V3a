apt update && apt upgrade -y
apt install git -y
pip3 install -U pip
apt install git python3-pip ffmpeg -y

git clone https://github.com/anumitultra/RENAMER_BOT_V3a.git          
pip3 install -r requirements.txt
npm install http-server -g
http-server -p $PORT &
python bot.py
