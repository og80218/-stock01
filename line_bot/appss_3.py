from flask import Flask, request, abort, render_template, flash, redirect, url_for
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from datetime import datetime
import configparser

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
#YOUR_CHANNEL_ACCESS_TOKEN #需改成自己的 #TOP=>股市小子=>圖片辨識機械人=> Messaging API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#YOUR_CHANNEL_SECRET #需改成自己的
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

app = Flask(__name__)

#直接回應圖片訊息   #需在imgur上傳圖片
@app.route("/sendImage/")
def sendImage(event):
    try:
        message = ImageSendMessage(
            original_content_url = "https://i.imgur.com/5PNBSaO.png",
            preview_image_url = "https://i.imgur.com/5PNBSaO.png"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統還在準備中...'))
