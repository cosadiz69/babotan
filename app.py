# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('P4r78VVeOyBtEbG1PZaDL0+/1gt3553hJGC9Wxq4O4yac/2aZ6U1pGSjtwy8h25rOciAZjdtduJPDFTryAh2opnuQaZ4wln8YhZDq+eatF9H1TIVOBFc2SnPzX2KoovR6tdJgP6ue1ytOVLhyQaoGgdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('783b45617d00c70bd5acb4bccee7b561') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])