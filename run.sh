#!/bin/bash

python3 -m venv XanDiscordBotEnv

source XanDiscordBotEnv/bin/activate

pip install -r piplist.txt

clear

nohup python3 Bot.py > TamaLog.txt 2>&1 &
