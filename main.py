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
     '引越しについて' : '質問内容を選択肢よりお選びください。\nA.引越しの手続きについて',
     'A' : '質問内容を選択肢よりお選びください。\na.必要な書類・注意事項\nb.書類の提出期限\nc.その他連絡事項',
     'a' : '◆必要な書類◆\n①住所変更届\n②住所変更後の住民票の写し\n③賃貸契約書の写し\n\n◆書類記載時の注意事項◆\
            \n*②はコピー、PDFでも可。写真不可。\n*①〜③はメールでの送信可。\n*既婚者の方は、住所変更届にある下記を必ずご記入ください。\
            \n【配偶者を扶養して いる ・ いない】',
     'b' : '◆提出期限◆\n転居・転入手続き後、速やかに提出すること。\n※引越し日、定期変更(区間変更日or払戻日)によって提出期限は異なる\
            \n※上記期限までに提出が難しい場合は、「賃貸契約書の写し」「住所変更届および住民票」を分けて提出',
     'c' : '確定次第、下記についてご報告下さい。\n*引っ越し日\n*新定期使用開始日\n*引越し先の住所\n*引越し後の最寄駅',
     '結婚について' : 'B.入籍時に必要な手続きについて（通常）\nC.入籍時に必要な手続きについて（名字が変更になる場合）',
     'B' : 'd.必要な書類・注意事項\ne.書類の提出期限\nf.その他連絡事項',
     'd' : '◆必要な書類◆\n①家族異動届\n②住民票の写し（世帯全員の住民票（続柄記載されているもの））\n③扶養する場合の必要資料の提出\
            \n\n\n◆書類記載時の注意事項◆\n*②別居の場合は、戸籍謄本をご提出ください。\n*③「扶養者の申請に必要な提出書類一覧表」をご確認ください\
            \nまた一覧表については、家族異動届のシート「裏」をご確認ください',
     'e' : '◆提出期限◆\n①～③の書類提出期限は、入籍日によって異なります。',
     'f' : '引越しのご予定などありましたら、お知らせください。\n入籍日と引越し日が近い場合、住民票は１枚で手続き可能な場合も\
            \nありますのでご相談ください。',
     'C' : 'g.必要な書類・注意事項\nh.書類の提出期限\ni.その他連絡事項',
     'g' : '◆必要な書類◆\n※通常時と同様\n①家族異動届 \n②住民票の写し（世帯全員の住民票（続柄記載されているもの））\
            \n③扶養する場合の必要資料の提出\n\n\n◆書類記載時の注意事項◆\n*②別居の場合は、戸籍謄本をご提出ください。\
            \n*③「扶養者の申請に必要な提出書類一覧表」をご確認ください\nまた一覧表については、家族異動届のシート「裏」をご確認ください',
     'h' : '◆提出期限◆\n※通常時と同様\n①～③の書類提出期限は、入籍日によって異なります。',
     'i' : '◆氏名変更について◆\n*健康保険証\n病院に行く予定がある場合は、健康保険証の代わりになる書類をお渡ししますので、必要でしたらご連絡ください。\
            \n\n*年金手帳\n名前はご自身で書き換えてください。\n年金事務所への届け出は会社で行います。\
            \n\n*勤務表/旅費精算書\n新姓への変更が必要です。\n会社保管の印鑑も新姓のものに交換する。\
            \n\n◆旧姓のままで問題ないもの◆\n社員証\n名刺\nデータ印\n給与振込口座\n※口座名を変更する場合は、必ず事前にご連絡ください。',
     '出産について' : 'D.出産時の必要な手続きについて',
     'D' : '質問内容を選択肢よりお選びください。\nj.必要な書類・注意事項\nk.書類の提出期限',
     'j' : '◆必要な書類◆\n①家族異動届\n②マイナンバー提供書\n③住民票の写し\n※母子手帳の提出は不要。\
            \n\n◆書類記載時の注意事項◆\n*住民票は世帯全員分で続柄が記載してあるもので、マイナンバーの記載を省略してください。\
            \n*マイナンバー提供署は家族異動届に含まれています。',
     'k' : '◆提出期限◆\nマイナンバー発行が遅くなる場合は、マイナンバー提供書は後日提出でも可能。',
     '扶養について' : 'E.扶養する場合の手続きについて\nF.扶養から外す場合の手続きについて',
     'E' : 'l.必要な書類・注意事項\nm.その他連絡事項',
     'l' : '◆必要な書類◆\n①家族異動届\n②扶養する場合の必要資料の提出\
            \n\n◆書類記載時の注意事項◆\n*②「扶養者の申請に必要な提出書類一覧表」をご確認ください\
            \nまた一覧表については、家族異動届のシート「裏」をご確認ください',
     'm' : '*扶養するの時は書類の不備、遅れがあると手続きに影響が出るので 不明なことは早めにご相談してください！！\
            \n*扶養する理由もメールでご連絡ください。（詳細な理由が分かると必要な書類を絞り出すことができます）',
     'F' : 'n.必要な書類・注意事項',
     'n' : '◆必要な書類◆\n①家族異動届\n②健康保険証の返却\
            \n\n◆書類記載時の注意事項◆*就職により扶養を外す場合、異動日は新しいお勤め先の会社保険に 加入した日を記載してください。',
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
