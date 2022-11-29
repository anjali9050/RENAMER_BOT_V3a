apt update && apt upgrade -y
RUN apt-get -qq install -y git python3 python3-pip \
    locales python3-lxml aria2 \
    curl pv jq nginx npm
npm install http-server -g
http-server -p $PORT &
apt install git -y
pip3 install -U pip
apt install git python3-pip ffmpeg -y

git clone https://github.com/anumitultra/RENAMER_BOT_V3a.git          
pip3 install -r requirements.txt
python bot.py
