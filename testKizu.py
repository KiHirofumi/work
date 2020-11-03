import json
#import selectList

json_open = open('./selectList.json', 'r')
json_load = json.load(json_open)

# JSON全体表示
#print(json_load)
# JSON決め打ち表示
print(json_load['結婚について']['comment'])
# JSON Loop表示
#for v in json_load.values():
    #print(v[''])
#    print(v)

#text = selectList.inquiry_list[]
#print(selectList.inquiry_list['A'])
print(json_load['結婚について']['B']['comment'])
print(json_load['結婚について']['B']['d'])