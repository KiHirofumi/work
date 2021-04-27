from linebot import LineBotApi
from linebot.models import TextSendMessage,  FlexSendMessage

import json

def make_flex():
    with open('hikkosimenu.txt') as flex_message_json_string:
        flex_message_json_dict_hikkosi =  json.load(flex_message_json_string)
        return flex_message_json_dict_hikkosi