#import requests
import json

def flexMessageCreate():
    """translate関数
    キーとなる文字列に対応した回答を返す。
    :param input: str
        キーとなる文字列
    """
    
    fmcList = {}
    #2021/12/27 修正 fromatfmcHeader
    formatfmcHeader  = {"type":"bubble","size": "giga","header": {"type": "box","layout": "vertical","contents": []}}

    formatfmcTitle_1 = {"type": "text","text": "","margin": "none","size": "xxl","weight": "bold","decoration": "none","position": "relative","align": "center","gravity": "top","wrap": False}
 
    #2021/12/27 修正 formatfmcTitle_2
    formatfmcTitle_2 = {"body": {"type": "box","layout": "vertical","contents": []}}

    formatfmcBody_1 = {"type": "text","text": "","size": "lg","color": "#ff4500","weight": "bold","decoration": "underline","margin": "none","position": "relative","align": "start","offsetTop": "sm","offsetStart": "none"}
    formatfmcBody_2 = {"type": "text","text": "","wrap": True,"margin": "","offsetStart": "md","offsetTop": "none"}
    formatfmcBody_End = {"type": "text","text": "","margin": "xs","align": "center","offsetTop": "none","offsetStart": "md"}

    #2021/12/27 修正 formatfmcFooter
    #formatfmcFooter  = ']}"}'

    #2021/12/27 追加
    formatfmcHeader_Header = formatfmcHeader.copy()

    #2021/12/27 追加
    fmcTitle_1 = formatfmcTitle_1.copy()
    fmcTitle_1["text"] = '【引越しに必要な書類】'  #ここは最終的にGASから取得した値をセット
    formatfmcHeader_Header["header"]["contents"].extend([fmcTitle_1]) #Contentsはリスト型で、辞書型のデータを格納する

    #大枠のリストに追加
    fmcList.update(formatfmcHeader_Header)

    #2022/01 追加
    formatfmcBody = formatfmcTitle_2.copy()

    #2022/01 追加 ループ処理
    with open(r'C:\Users\USER\ICdog\work\virtualenvs\実行環境名（なんでもよい）\test.txt',encoding="utf-8") as input:
    
        #改行処理 (22/2/18_\nは消去できるが空白が処理できていない)
        #input_strip = [s.replace(' ','') for s in input.readlines()]
        input_strip = [s.strip() for s in input.readlines()]

        for index, i in enumerate(input_strip):

            if ('◆' in i) :
                cnt = 0
                fmcBody_1 = formatfmcBody_1.copy()
                fmcBody_1["text"] = i
                cnt = cnt + 1
                formatfmcBody["body"]["contents"].extend([fmcBody_1])
            
            elif ((('【' not in i) and cnt == 1) and i != '') :
                fmcBody_2 = formatfmcBody_2.copy()
                fmcBody_2["text"]   = i
                fmcBody_2["margin"] = 'md'
                cnt = cnt + 1
                formatfmcBody["body"]["contents"].extend([fmcBody_2])

            elif ((('【' not in i) and cnt > 1) and i != '') :
                fmcBody_2 = formatfmcBody_2.copy()
                fmcBody_2["text"]   = i
                fmcBody_2["margin"] = 'xs'
                cnt = cnt + 1
                formatfmcBody["body"]["contents"].extend([fmcBody_2])
            
            elif ('【' in i) :
                fmcBody_End = formatfmcBody_End.copy()
                fmcBody_End["text"] = i
                formatfmcBody["body"]["contents"].extend([fmcBody_End])
    
    #大枠のリストに追加
    fmcList.update(formatfmcBody)

    #最終的なdump処理
    outpath = r'C:\Users\USER\ICdog\work\virtualenvs\実行環境名（なんでもよい）\fmcTextho.json'
    with open(outpath, 'w') as w:
        json.dump(fmcList, w, ensure_ascii=False, indent=2, sort_keys=False, separators=(',', ': '))
        

if __name__ == '__main__': # 「__」を半角に直してください。
    # メソッドの呼び出し例
    a = flexMessageCreate()
