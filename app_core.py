# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('showminglinebot01', 'channel_access_token'))
handler = WebhookHandler(config.get('showminglinebot01', 'channel_secret'))


# LINE 聊天機器人的基本資料
#line_bot_api = LineBotApi('97S2rQqI1uYIPevGC+5zZI4NcjgtWme3UODvdpcdPXb8pOpCz/HI9L4NdM77XgzIMcLGY3kKc8N5bDNsu8zzBuNfnfxgzIMf6pX7AdGZY6ar5N9EXFWV33HBff2wfYXVRKxkWsIGIKo0suAempn3AQdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('309d6ce4414288e8840108d261d77df2')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
    app.run()

