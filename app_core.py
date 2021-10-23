# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()