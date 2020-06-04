#測試中-未完成
#line bot 股市小子
import os, sys, re
from flask import Flask, request, abort, jsonify
import requests
from datetime import datetime
from flask_cors import CORS
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from flask import render_template

from flask import Flask, request, abort, render_template, flash, redirect, url_for
#from linebot import (LineBotApi, WebhookHandler)
#from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import configparser
from appss_1 import sendQuiclreply3
from appss_2 import ButtonsTemplate_send_message
from appss_3 import sendImage
from appss_4 import get_profile
import appss_5
import appss_6_news
import Msg_Template
import stockprice


app = Flask(__name__)
CORS(app)

# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
# if channel_secret is None or channel_access_token is None:
#     print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
#     sys.exit(1)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
#YOUR_CHANNEL_ACCESS_TOKEN #需改成自己的 #TOP=>股市小子=>圖片辨識機械人=> Messaging API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#YOUR_CHANNEL_SECRET #需改成自己的
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

#直接取得ID #OK
# userId = 'U04e0358523a61a8fa702c773773e14b5'
# profile_data = {'Authorization': 'Bearer ' + '3nS6wBZoqGb+WEogaI8n7XDQEPXqRGK3iS0tdfNwrITjL6U49FITfKONTKRejeZk51B+Q3ywNWeu5ouHahMyTPNoCmlBJMHG9N3bayvNz0XlSr9jquUwVn/nmYVEHYJajGJmpO6NLG/jTAnE70h6kwdB04t89/1O/w1cDnyilFU='}
# profile = requests.get('https://api.line.me/v2/bot/profile/'+ userId, headers=profile_data)
# print(profile.text)

# a =profile.text
# with open('as.txt', 'a') as outfile:
#     outfile.write(a)

#下段程式碼，複製貼上
@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'



#雪倫教的
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #OK
    # msg = event.message.text
    # print(msg)

    # msg = msg.encode('utf-8')
    # print(msg)

    #回傳使用者ID，並存檔使用者ID及留言紀錄  #OK
    # user_id = event.source.user_id
    # print("user_id =", user_id, ',輸入內容 =', msg)
    # # profile = line_bot_api.get_profile(user_id)
    # a = user_id
    # b = msg
    # with open('as.txt', 'a') as outfile:
    #     outfile.write(a)
    #     outfile.write(b)

    msg = str(event.message.text).upper().strip()
    print(msg)
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name  # 使用者名稱
    uid = profile.user_id  # 發訊者ID

    #當使用者輸入"你好", "哈嘍", 'HI', 'hi', '嗨'的linebot回應方式
    if msg in ("你好", "哈嘍", 'HI', 'hi', '嗨'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你好～歡迎加入股市小子! 有什麼想要詢問的都可以在這裡詢問唷！請使用圖形選單！')),
        return 0
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text="汪汪叫"))

    #當使用者輸入文字為 股市 線圖 漲跌 ，即回應 '請點選下方選單'K線'

    # if msg == 'start':
    if re.match("股票推薦", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.greeting_msg))
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q1))
        content = appss_5.Q1_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("Q2", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q2))
        line_bot_api.push_message(uid, appss_5.Q2_menu())
        return 0
    elif re.match("Q3", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q3))
        line_bot_api.push_message(uid, appss_5.Q3_menu())
        return 0
    elif re.match("Q4", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q4))
        line_bot_api.push_message(uid, appss_5.Q4_menu())
        return 0
    elif re.match("Q5", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q5))
        line_bot_api.push_message(uid, appss_5.Q5_menu())
        return 0
    elif re.match("Q6", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q6))
        line_bot_api.push_message(uid, appss_5.Q6_menu())
        return 0
    elif re.match("Q7", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q7))
        line_bot_api.push_message(uid, appss_5.Q7_menu())
        return 0
    elif re.match("Q8", msg):
        line_bot_api.push_message(uid, TextSendMessage(appss_5.Q8))
        line_bot_api.push_message(uid, appss_5.Q8_menu())
        return 0
    elif re.match("類型A", msg):
        img_url = appss_5.type_A
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = appss_5.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = appss_5.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型C", msg):
        img_url = appss_5.type_C
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型D", msg):
        img_url = appss_5.type_D
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型E", msg):
        img_url = appss_5.type_E
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型F", msg):
        img_url = appss_5.type_F
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型G", msg):
        img_url = appss_5.type_G
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型H", msg):
        img_url = appss_5.type_H
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型I", msg):
        img_url = appss_5.type_I
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型J", msg):
        img_url = appss_5.type_J
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0

    elif re.match('N[0-9]{4}', msg):  # 個股新聞
        stockNumber = msg[1:5]
        content = appss_6_news.single_stock(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage('即將給您代號' + stockNumber + '個股新聞'))
        line_bot_api.push_message(uid, content)
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0

    # elif re.match("N外匯[A-Z]{3}", msg):
    #     currency = msg[3:6]
    #     line_bot_api.push_message(uid, TextSendMessage("將給您最新外匯消息"))
    #     line_bot_api.push_message(uid, appss_6_news.exrate_news())
    #     btn_msg = Msg_Exrate.realtime_currency_other(currency)
    #     line_bot_api.push_message(uid, btn_msg)
    #     return 0


    #連結網址
    if msg == '我的收藏':
        ButtonsTemplate_send_message(event)
        return 0
    #給予選項點選
    if msg == '歷史紀錄':
        sendQuiclreply3(event)
        return 0

    if msg == '顯示圖片':
        sendImage(event)
        return 0

    # if msg == '我是誰':
    #     get_profile(user_id)
    if msg == '你是誰':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="我是誰我是Smart啦！！"))
        return 0

    else:
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統還在準備中...'))
        return 0



#處理文字訊息，KEY什麼回什麼 #若要有特殊回應，需而外google
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     #不處理官方發來的訊息
#     if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
#
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=event.message.text) #event.message.text得到傳來的文字
#         )


#連結html檔案
# @app.route()
# def apple():
#     return render_template('123.html')

if __name__ == '__main__':
    # 允許所有IP存取服務, 打開port 1111
    port = int(os.environ.get('PORT', 1111))
    app.run(debug=True, port=port, host='0.0.0.0')


    #app.secret_key = '自己的'     #若遇到取得金鑰在解註解
