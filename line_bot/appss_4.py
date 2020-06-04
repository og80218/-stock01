from flask import Flask, request, abort, render_template, flash, redirect, url_for
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from datetime import datetime
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import configparser

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
#YOUR_CHANNEL_ACCESS_TOKEN #需改成自己的 #TOP=>股市小子=>圖片辨識機械人=> Messaging API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#YOUR_CHANNEL_SECRET #需改成自己的
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

app = Flask(__name__)

def get_profile(self, user_id, timeout=None):
    """Call get profile API.
    https://developers.line.biz/en/reference/messaging-api/#get-profile
    Get user profile information.
    :param str user_id: User ID
    :param timeout: (optional) How long to wait for the server
        to send data before giving up, as a float,
        or a (connect timeout, read timeout) float tuple.
        Default is self.http_client.timeout
    :type timeout: float | tuple(float, float)
    :rtype: :py:class:`linebot.models.responses.Profile`
    :return: Profile instance
    """
    response = self._get(
        '/v2/bot/profile/{user_id}'.format(user_id=user_id),
        timeout=timeout
    )

    return Profile.new_from_json_dict(response.json)
