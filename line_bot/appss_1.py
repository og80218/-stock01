from flask import Flask, request, abort, render_template, flash, redirect, url_for
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import configparser

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
#YOUR_CHANNEL_ACCESS_TOKEN #需改成自己的 #TOP=>股市小子=>圖片辨識機械人=> Messaging API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#YOUR_CHANNEL_SECRET #需改成自己的
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

def sendQuiclreply3(event):
    try:
        message = TextSendMessage(
            text='請選擇',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='歷史紀錄',
                                             text='https://www.cnyes.com/archive/twstock/html5chart/2330.htm')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='圖片',
                                             text='https://imgur.com/5PNBSaO')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='別玩我',
                                             text='還點')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='error'))
