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
#
line_bot_api = LineBotApi('DeYk5m+54nt/UGOTsDrqL0nfUZOuHY/TG7POtzYT+6YlyXe+QgdaiH9iH8hI0jagEH/4vW0c+bXUYyclS8RXfp7doZBjm92/2CnPeseu+bcG2Giw1jPNSPA2h0A/E3Tz7bmweNe4z2j9rHvn3mY2nwdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('071b8b56e61c99e4affe87f4d453832f') #Your Channel Secret

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
