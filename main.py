from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import os

# サンプル追加 20210403
import chatBotPythonIf
import chatBotflexMessageCreate
import json

# サンプル追加 20210403


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #サンプル追加 20220904
#    try:

    #ファイル読み込み有無
    templateflg = 0

    #LINEクライアントから受信したメッセージを代入
    linemsg = event.message.text

    #各カテゴリーのテンプレートメッセージファイルを設定
    #--- Pythonにはswitch文が存在しないため、if-elif-elseで分岐
    if (linemsg == 'メニュー') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Menu.json"

    elif (linemsg == '引っ越し手続き') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Move.json"

    elif (linemsg == '結婚氏名変更なし') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Marriage.json"

    elif (linemsg == '結婚氏名変更あり') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Change_Surname.json"

    elif (linemsg == '出産手続き') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Childbirth.json"

    elif (linemsg == '扶養手続き') :
        templateflg = 1
        FILENAME = "Flex_Bubblemsg_Support.json"

    else :
        #問い合わせ内容の回答メッセージを生成する（GAS連携）
        a = chatBotPythonIf.do_translate(event.message.text.encode('utf-8'))
        b = a.replace(' ', '')
        c = b.split('\n')

        #List内のからの要素を削除
        cc = [i for i in c if i != '']

        d = json.loads(chatBotflexMessageCreate.flexMessageCreate(cc, event.message.text))

    if (templateflg == 1) :
        #テンプレートメッセージをjson形式で読み込む
        fd = open(FILENAME, mode='r')
        d = json.load(fd)
        fd.close()

    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='alt_text',contents=d))

#    except:
#        line_bot_api.reply_message(
#            event.reply_token,
#            TextSendMessage(text=event.message.text)) #ここでオウム返しのメッセージを返します。

# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
