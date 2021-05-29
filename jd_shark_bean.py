import traceback

import jdCookie
import json
import requests
import time
import notification

"""
摇京豆
"""


def getTemplate(cookies, functionId, body):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'api.m.jd.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://spa.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
    }
    params = (
        ('functionId', functionId),
        ('appid', 'sharkBean'),
        ('body', json.dumps(body)),
        ('t', int(time.time() * 1000)),
    )
    response = requests.post(
        'https://api.m.jd.com', headers=headers, cookies=cookies, params=params)
    return response.json()


def postTemplate(cookies, functionId, body):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'api.m.jd.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://spa.jd.com',
    }
    params = (
        ('functionId', functionId),
        ('appid', 'sharkBean'),
        ('body', json.dumps(body)),
    )
    response = requests.post(
        'https://api.m.jd.com', headers=headers, cookies=cookies, params=params)
    return response.json()


def run():
    for cookies in jdCookie.get_cookies():
        # pg_channel_page_data = getTemplate(cookies, 'pg_channel_page_data', {"paramData": {"token": "dd2fb032-9fa3-493b-8cd0-0d57cd51812d"}})
        # print(pg_channel_page_data)
        # if pg_channel_page_data.get('success'):
        #     remainLotteryTimes = pg_channel_page_data.get('data', {}).get('floorInfoList', [{}])[0].get('floorData', {}).get('shakingBoxInfo', {}).get('remainLotteryTimes', 0)
        #     for _ in range(remainLotteryTimes):
        #         vvipclub_shaking_lottery = postTemplate(cookies, 'vvipclub_shaking_lottery', {})
        #         print(vvipclub_shaking_lottery)
        try:
            pg_interact_interface_invoke = postTemplate(cookies, 'pg_interact_interface_invoke',
                                                        {"floorToken": "f1d574ec-b1e9-43ba-aa84-b7a757f27f0e",
                                                         "dataSourceCode": "signIn",
                                                         "argMap": {"currSignCursor": 2}})
            print(pg_interact_interface_invoke)
        except:
            traceback.print_exc()
        while True:
            vvipclub_shaking_lottery = postTemplate(cookies, 'vvipclub_shaking_lottery', {})
            print(vvipclub_shaking_lottery)
            if vvipclub_shaking_lottery.get('success'):
                if vvipclub_shaking_lottery.get('data', {}).get('remainLotteryTimes'):
                    continue
            break


if __name__ == '__main__':
    run()
