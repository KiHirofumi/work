import requests

def do_translate(input):
    """translate関数
    キーとなる文字列に対応した回答を返す。
    :param　input: str
        キーとなる文字列
    """
    # api_urlはherokuの環境変数へ埋め込むことを推奨
    api_url = r"https://script.google.com/macros/s/AKfycbyHuavrIuEKgHgM1vFBzuMbjLm2P-tTzcNafs1Fz3ftfQkoozHs6ZTf0lnrVtrEVpCN3Q/exec"

    params = {
        'text': input
    }
    r_post = requests.post(api_url, input)

    # コンソールに出力 実際は呼び出し元にreturnするように記載
    return r_post.json()["result"]
    #print(r_post.json()["result"])
    #print(r_post.json())

#if __name__ == '__main__': # 「__」を半角に直してください。
    # メソッドの呼び出し例
#    a = do_translate('引っ越し・必要な書類'.encode('utf-8'))
#    print(a)
#    b = a.replace(' ', '')
#    c = b.split('\n')

#    for i in c:
#        print(i)
    
  