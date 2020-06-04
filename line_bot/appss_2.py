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

@app.route("/ButtonsTemplate/")
def ButtonsTemplate_send_message(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/3NXAL4t.png',
            title='我的收藏',
            text='不要點您會怕！',
            actions=[
                PostbackTemplateAction(
                    label='目前收藏的個股清單',
                    text='目前收藏的個股清單:',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='現在幾點了？',
                    text=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ),
                URITemplateAction(
                    label='技術線圖',
                    uri='https://www.cnyes.com/archive/twstock/html5chart/2330.htm'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
