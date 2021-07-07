# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import hashlib
import datetime
from slacker import Slacker

count = 53
token = 'you'r Bot-account token'
slack = Slacker(token)
channel = 'channel ID'

@respond_to(r'.+')
def all_respond_func(message):
    text = message.body['text']
    msg = '匿名で投稿しました。\n```' + text + '```'
    message.reply(msg)

    user_id = message.body['user']
    hashed_id = hashlib.md5((str(datetime.date.today()) + user_id).encode()).hexdigest()[:9]

    global count
    count += 1
    if count > 1000:
            count = 1
    message_id = count

    title_template = "{message_id}：以下、VIPにかわりまして名無しがお送りします ID:{hashed_id}"
    username = title_template.format(message_id=message_id, hashed_id=hashed_id)

    slack.chat.post_message(channel,text,username,icon_emoji=":tsubo:")
