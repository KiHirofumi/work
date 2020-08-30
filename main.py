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
    #app.logger.info("Request body: " + body)

    # handle webhook body
    # 署名を検証し、問題なければhandleに定義されている〜〜
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'


## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。

inquiry_text = "お問合せ内容を選択してください。\n1.福利厚生について\n2.規則について\n3.手当について\n4.手続きについて"
inquiry_list = {
     '福利厚生について' : '101:医療・保健について\n102:慶弔見舞金について\n999:終了',
     '101' : '110:健康診断\n111:メンタルヘルスケア\n999:終了',
     '102' : '120:結婚祝い\n121:出産祝い\n999:終了',
     '110' : '年1回健康診断を受診してください。',
     '111' : '半年に1回実施してください',
     '120' : '結婚おめでとうございます。10000円です',
     '121' : '出産おめでとうございます。15000円です',
     '規則について' : '201:就業規則について\n202:服務規律について\n999:終了',
     '201' : 'ガイドブックを参照してください',
     '202' : 'ガイドブックを参照してください',
     '手当について' : '301:家賃補助について\n302:資格手当について\n999:終了',
     '301' : '310:実家\n311:一人暮らし\n999:終了',
     '302' : '320:基本情報\n321:応用情報\n999:終了',
     '310' : '実家暮らしの場合、10000円です',
     '311' : '一人暮らしの場合、15000円です',
     '320' : '基本情報の場合、10000円です',
     '321' : '応用情報の場合、15000円です',
     '手続きについて' : '401:引っ越しについて\n402:結婚について\n999:終了',
     '401' : '410:引っ越し前\n411:引っ越し後\n999:終了',
     '402' : '420:結婚前\n421：結婚後\n999:終了',
     '410' : '引っ越し後に〇〇〇を提出してください',
     '411' : '〇〇〇を提出してください',
     '420' : '結婚後に△△△を提出してください',
     '421' : '△△△を提出してください',
     '999' : 'お疲れ様でした。仕事頑張ってください。',
}

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in inquiry_list.keys():
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=inquiry_list[event.message.text]))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)) #ここでオウム返しのメッセージを返します。

# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)