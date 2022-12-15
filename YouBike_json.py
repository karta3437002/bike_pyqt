import requests

'''
#資料欄位說明
sno：站點代號
sna：場站名稱(中文)
tot：場站總停車格
sbi：場站目前車輛數量
sarea：場站區域(中文)
mday：資料更新時間
lat：緯度
lng：經度
ar：地址(中文)
sareaen：場站區域(英文)
snaen：場站名稱(英文)
aren：地址(英文)
bemp：空位數量
act：全站禁用狀態 
'''
#sno-ar-tot-sbi-bemp-mday
#開放資料：'YouBike新北市公共自行車即時資訊'
#url = 'http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json'


def strB2Q(ustring):
    """半形轉全形"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:                 # 半形空格直接轉化
            inside_code = 12288
        elif 32 <= inside_code <= 126:        # 半形字元（除空格）根據關係轉化
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring


url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json"

def get_json(url):

    html_content = requests.get(url)

    json_data = html_content.json()
    return json_data

def get_stage(json):
    stage_l = []
    for item in json:

        stage_l.append(item["sna"])

    return stage_l


def print_info(json):

    for item in json:
        print_info = '站名：' + strB2Q(f'{item["sna"]: <15}') + f' , 空位數量：{item["bemp"]} 個'

        print(print_info)


if '__name__' == "__main__":

    json = get_json(url)

    print(json)
    result = [x for x in json if x["sna"]=='大鵬華城']
    print(result)