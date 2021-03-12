from linebot import LineBotApi
from linebot.models import TextSendMessage,  FlexSendMessage

import json

FILENAME = "hikkosimenu.json"

fd = open(FILENAME, mode = 'r')
data = json.load(fd)
fd.close()

def make_flex():
    messages =  FlexSendMessage(
        alt_text = "引越しについての問合せ",
        contents = data
    )
    return messages