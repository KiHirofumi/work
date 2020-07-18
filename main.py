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
import os

app = Flask(__name__)

# 環境変数取得
# LINE Developersで設定されているアクセストークンとChannel Secretをを取得し、設定します。
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
 
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
 

## 1 ##
# Webhookからのリクエストをチェックします。
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    # 署名を検証し、問題なければhandleに定義されている〜〜
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

##20200712一旦オウム返しに戻すため、コメントアウト
#@app.route("/index", methods=['POST'])
#def index():
#    return 'OK'

## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=event.message.text)) #ここでオウム返しのメッセージを返します。
##20200712一旦オウム返しに戻すため、コメントアウト
#        TextSendMessage(text=event.message.text & "メッセージありがとう")) #ここでオウム返しのメッセージを返します。
    if event.message.text == "質問":
        #処理test
        event.reply_token,
        TextSendMessage(text="庶務さんに問い合わせてください")
        
        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)) #ここでオウム返しのメッセージを返します。



# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
