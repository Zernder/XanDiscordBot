@echo off

call git clone https://github.com/Zernder/XanDiscordBot.git

cd ./XanDiscordBot

mkdir Music

python -m venv XanDiscordBotEnv

call XLHEnv\Scripts\activate

pip install -r piplist.txt