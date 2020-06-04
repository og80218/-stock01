from linebot.models import *
import configparser
from linebot import (LineBotApi, WebhookHandler)
from flask import Flask

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
#YOUR_CHANNEL_ACCESS_TOKEN #需改成自己的 #TOP=>股市小子=>圖片辨識機械人=> Messaging API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#YOUR_CHANNEL_SECRET #需改成自己的
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

app = Flask(__name__)

greeting_msg = '每個人的投資風格與適合的投資商品不盡相同，在開始使用本理財機器人之前，可以先做以下問卷了解自己適合的投資商品跟分析方法呦~'
Q1_msg = '請問您手邊有多少閒置資金(能100%投入市場的錢)?\n'
Q1_option1 = '1. 10萬以下\n'
Q1_option2 = '2. 10萬 – 50萬\n'
Q1_option3 = '3. 50萬以上'
Q1 = Q1_msg + Q1_option1 + Q1_option2 +Q1_option3

Q2_msg = '請問您這筆錢您能承受多大虧損?\n'
Q2_option1 = '1. 不能虧損超過10%\n'
Q2_option2 = '2. 不能虧損超過30%\n'
Q2_option3 = '3. 不能虧損超過50%\n'
Q2_option4 = '4. 虧損超過100%也可以'
Q2 = Q2_msg + Q2_option1+ Q2_option2+ Q2_option3+ Q2_option4

Q3_msg = '請問您投資標的地獲利速度，下述時間請選擇?\n'
Q3_option1 = '1. 1個月\n'
Q3_option2 = '2. 1~6個月\n'
Q3_option3 = '3. 6個月~1年\n'
Q3_option4 = '4. 1年以上'
Q3 = Q3_msg + Q3_option1+ Q3_option2+ Q3_option3+ Q3_option4

Q4_msg = '以下哪一個敘述，比較符合你獲利和風險的要求?\n'
Q4_option1 = '1. 虧損50%以上都還可以承受，最好能每年獲利100%以上\n'
Q4_option2 = '2. 最多有可能虧損10%的情況，每年希望至少15%以上的獲利\n'
Q4_option3 = '3. 賺多少無所謂，但不能有任何虧損!'
Q4 = Q4_msg + Q4_option1+ Q4_option2+ Q4_option3

Q5_msg = '假設你選擇高風險、高獲利的方法，你覺得賺多少錢才夠?\n'
Q5_option1 = '1. 賺到5000萬可以慢慢收手才夠下半輩子花\n'
Q5_option2 = '2. 賺到1000萬可以慢慢收手'
Q5 = Q5_msg + Q5_option1+ Q5_option2

Q6_msg = '你目前能投入多少時間學投資?\n'
Q6_option1 = '1. 每天1~2小時\n'
Q6_option2 = '2. 每周1~2小時\n'
Q6_option3 = '3. 每月1~2小時'
Q6 = Q6_msg + Q6_option1+ Q6_option2+ Q6_option3

Q7_msg = '以下哪個比較符合你的現狀?\n'
Q7_option1 = '1. 我每天都可以看盤，也很喜歡看盤做出判斷\n'
Q7_option2 = '2. 我喜歡透過價格或籌碼數據統計、價格圖表做出分析\n'
Q7_option3 = '3. 我喜歡透過基本面的數據分析\n'
Q7_option4 = '4. 我不想要太多研究分析，我只要一個簡單又保證能賺錢的方法'
Q7 = Q7_msg + Q7_option1+ Q7_option2+ Q7_option3 + Q7_option4

Q8_msg = '以下哪一個敘述比較符合你的個性?\n'
Q8_option1 = '1. 在好公司股價便宜時買進，太貴的時候賣出，賺取中間價差\n'
Q8_option2 = '2. 經過精心研究，找到幾間可能成長10倍以上的好公司，重押它們'
Q8 = Q8_msg + Q8_option1+ Q8_option2

type_A = 'https://i.imgur.com/K8wVBDC.png'		#
type_B = 'https://i.imgur.com/z2rOwoF.png'		#
type_C = 'https://i.imgur.com/N5J1Bsz.png'		#
type_D = 'https://i.imgur.com/3M14YRv.png'		#
type_E = 'https://i.imgur.com/wOxLC2G.png'		#
type_F = 'https://i.imgur.com/sBo6xq0.png'		#
type_G = 'https://i.imgur.com/Ht9N7nS.png'		#
type_H = 'https://i.imgur.com/a2GgcfQ.png'		#
type_I = 'https://i.imgur.com/3q3OAAg.png'		#
type_J = 'https://i.imgur.com/eNy6sQ6.png'		#

def Q1_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q1_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目一",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "1-1",
							"text": "Q2"} },
                        {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "1-2",
							"text": "Q3"} },
                        {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "1-3",
							"text": "Q4"} } ],
					"flex": 0} } )
    return flex_message

def Q2_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q2_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目二",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "2-1",
							"text": "類型J"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "2-2",
							"text": "Q5"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "2-3",
							"text": "類型F"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "2-4",
							"text": "類型G"} } ],
					"flex": 0} } )
    return flex_message

def Q3_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q3_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目三",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "3-1",
							"text": "類型I"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "3-2",
							"text": "Q7"
							} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "3-3",
							"text": "Q6"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "3-4",
							"text": "類型E"} } ],
					"flex": 0} } )
    return flex_message

def Q4_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q4_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目四",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "4-1",
							"text": "類型G"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "4-2",
							"text": "Q6"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "4-3",
							"text": "類型H"
							} } ],
					"flex": 0} } )
    return flex_message

def Q5_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q5_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目五",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "5-1",
							"text": "類型I"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "5-2",
							"text": "Q6"} } ],
					"flex": 0} } )
    return flex_message

def Q6_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q6_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目六",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ],
					"action": {
					"type": "datetimepicker",
					"label": "action",
					"data": "hello",
					"mode": "date"} },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
						"type": "message",
						"label": "6-1",
						"text": "Q7"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
						"type": "message",
						"label": "6-2",
						"text": "Q8"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "6-3",
							"text": "類型E"} } ],
                    "flex": 0} } )
    return flex_message

def Q7_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q7_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目七",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "7-1",
							"text": "類型D"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "7-2",
							"text": "類型C"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "7-3",
							"text": "Q8"} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "7-4",
							"text": "類型E"}}],
					"flex": 0} } )
    return flex_message

def Q8_menu():
    flex_message = FlexSendMessage(
        alt_text = "Q8_menu",
            contents = {
				"type": "bubble",
				"hero": {
					"type": "image",
					"url": "https://imgur.com/WN88L3I",
					"size": "xxs",
					"aspectRatio": "20:13",
					"aspectMode": "cover"},
				"body": {
					"type": "box",
					"layout": "vertical",
					"contents": [ {
						"type": "text",
						"text": "題目八",
						"weight": "bold",
						"size": "xl",
						"align": "center",
						"style": "normal",
						"decoration": "none"} ] },
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [ {
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "8-1",
							"text": "類型A"
							} },
						{
						"type": "button",
						"style": "link",
						"height": "sm",
						"action": {
							"type": "message",
							"label": "8-2",
							"text": "類型B"
							} } ],
					"flex": 0} } )
    return flex_message
