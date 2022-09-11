#import requests
from contextlib import nullcontext
import json
from os import remove
import chatBotPythonIf

def flexMessageCreate(input, title):
    """translate関数
    キーとなる文字列に対応した回答を返す。
    :param input: str
        キーとなる文字列
    """
    
    fmcList = {}
    #2021/12/27 修正 fromatfmcHeader
    formatfmcHeader  = {"type":"bubble","size": "giga","header": {"type": "box","layout": "vertical","contents": []}}

    formatfmcTitle_1 = {"type": "text","text": "","margin": "none","size": "xxl","weight": "bold","decoration": "none","position": "relative","align": "center","gravity": "top","wrap": True}
 
    #2021/12/27 修正 formatfmcTitle_2
    formatfmcTitle_2 = {"body": {"type": "box","layout": "vertical","contents": []}}

    #fmc_1 = {""""body": {"type": "box","layout": "vertical","contents": [,"""} 
    formatfmcBody_1 = {"type": "text","text": "　","size": "lg","color": "#ff4500","weight": "bold","decoration": "underline","margin": "none","position": "relative","align": "start","offsetTop": "sm","offsetStart": "none"}
    formatfmcBody_2 = {"type": "text","text": "　","margin": "","offsetStart": "md","offsetTop": "none","wrap": True}
    formatfmcBody_End = {"type": "text","text": "　","margin": "xs","align": "center","offsetTop": "none","offsetStart": "md"}
    #fmc_2 = {"]"}

    #2021/12/27 修正 formatfmcFooter
    #formatfmcFooter  = ']}"}'

    # print(formatfmcBody_1["text"])
    # print(formatfmcBody_2["text"])
    # print(formatfmcBody_3["text"])
    # print(formatfmcBody_End["text"])

    #print(formatfmcHeader)

    #2021/12/27 追加
    formatfmcHeader_Header = formatfmcHeader.copy()

    #2021/12/27 追加
    fmcTitle_1 = formatfmcTitle_1.copy()
    #fmcTitle_1["text"] = '【引越しに必要な書類】'  #ここは最終的にGASから取得した値をセット
    fmcTitle_1["text"] = title
    formatfmcHeader_Header["header"]["contents"].extend([fmcTitle_1]) #Contentsはリスト型で、辞書型のデータを格納する

    #print(formatfmcHeader_Header)

    #デバッグ用jsonファイル出力
    #path = './fmcText.json'
    #with open(path, 'w') as f:
    #    json.dump(formatfmcHeader_Header, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',', ': '))

    #print(fmcTitle_1)
    #fmcList.extend([fmcTitle_1])

    #print(formatfmcTitle_2)
    #fmcList.extend([formatfmcTitle_2])

    #2021/12/27 追加
    fmcTitle_2 = formatfmcTitle_2.copy()
    
    #with open(r'C:\Users\user\.local\share\virtualenvs\ic_dog_ver0.5\src\test.txt',encoding="utf-8") as input:

    cnt = 0
    for index, i in enumerate(input):

        if ('◆' in i) :
            cnt = 0
            fmcBody_1 = formatfmcBody_1.copy()
            fmcBody_1["text"] = i
            cnt = cnt + 1
            #print(fmcBody_1)
            fmcTitle_2["body"]["contents"].extend([fmcBody_1]) #Contentsはリスト型で、辞書型のデータを格納する
        
        elif (('【' not in i) and cnt == 1) :
            fmcBody_2 = formatfmcBody_2.copy()
            fmcBody_2["text"]   = i
            fmcBody_2["margin"] = 'md'
            cnt = cnt + 1
            #print(fmcBody_2)
            fmcTitle_2["body"]["contents"].extend([fmcBody_2]) #Contentsはリスト型で、辞書型のデータを格納する

        elif (('【' not in i) and cnt > 1) :
            fmcBody_2 = formatfmcBody_2.copy()
            fmcBody_2["text"]   = i
            fmcBody_2["margin"] = 'xs'
            cnt = cnt + 1
            #print(fmcBody_2)
            fmcTitle_2["body"]["contents"].extend([fmcBody_2]) #Contentsはリスト型で、辞書型のデータを格納する
        
        elif ('【' in i) :
            fmcBody_End = formatfmcBody_End.copy()
            fmcBody_End["text"] = i
            #print(fmcBody_End)
            fmcTitle_2["body"]["contents"].extend([fmcBody_End]) #Contentsはリスト型で、辞書型のデータを格納する

    #print(formatfmcFooter)
    fmcList = formatfmcHeader_Header.copy()
    fmcList.update(fmcTitle_2)
    #fmcList_str = "".join(map(str,fmcList))
    #print(fmcList_str)

    #デバッグ用jsonファイル出力
    #path = './fmcText2.json'
    #with open(path, 'w') as f:
    #    json.dump(fmcList, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',', ': '))

    return json.dumps(fmcList, ensure_ascii=False, indent=2, sort_keys=False, separators=(',', ': '))
