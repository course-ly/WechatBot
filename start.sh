./stop.sh
nohup python3 ./bot.py > /var/log/coursely/bot.log 2>&1 &
echo Starting Service \~
