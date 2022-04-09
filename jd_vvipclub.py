import traceback

import requests
import json
import jdCookie
import time

"""
入口: app首页 "领京东" ——  "摇京豆"
cron 5,8 0 * * *
"""


def template(cookies, functionId, body):
    headers = {
        'User-Agent': 'jdapp;iPhone;9.0.2;13.5.1',
        'Host': 'api.m.jd.com',
        'Referer': 'https://vip.m.jd.com/newPage/reward/123dd/slideContent?page=focus',
    }

    params = (
        ('appid', 'vip_h5'),
        ('functionId', functionId),
        ('body', json.dumps(body)),
        ('_', str(int(time.time() * 1000))),
    )

    response = requests.get('https://api.m.jd.com/',
                            headers=headers, params=params, cookies=cookies)
    return response.json()


def shark(cookies):
    """摇京豆"""
    headers = {
        'User-Agent': 'jdapp;iPhone;9.0.2;13.5.1',
        'Host': 'api.m.jd.com',
        'Referer': 'https://vip.m.jd.com/newPage/reward/123dd/slideContent?page=focus',
    }

    params = (
        ('appid', 'sharkBean'),
        ('functionId', 'vvipclub_shaking_lottery'),
        ('body', json.dumps({
            "riskInformation": {
                "platform": 4,
                "pageClickKey": "",
                "eid": "B2WSENAYGGNPHFXMEY2DOZGMS2ZRSPL6ZXMTXJNFMUWCS332YOBW5VI57MESBMUGURI76N2VRJWXMAM3E3CAZOAH5E",
                "fp": "6229eccbe60c067a7305af9933c093d4",
                "shshshfp": "fa9e1a0b9e6e3a515e846060de7fb43e",
                "shshshfpa": "fddc3a69-fcd3-f04f-67d2-5e8093fb29a2-1621210908",
                "shshshfpb": "d/tf8dOphtdkyBA4pRdJ6xw=="
            }
        })),
        ('t', '1649468411902'),
        ('h5st', '20220409094011906;7818360845267698;ae692;tk02w858e1b4018nX2l6V9VnevmsOF1ZOKJ6KlK+yaXzTjvMB76NDLjLXajE97i1M99qRJF/hvsTF/iaqlJNLL+ddQLk;2d861fff4b1ca998616ddb7af9081394e6f9dced22cd4e816aec94412d8b6506;3.0;1649468411906')
    )

    response = requests.post('https://api.m.jd.com/',
                             headers=headers, params=params, cookies=cookies)
    return response.json()


def shake(cookies):
    result = template(cookies, "pg_channel_page_data", {
        "paramData": {
            "token": "dd2fb032-9fa3-493b-8cd0-0d57cd51812d"
        },
        "riskInformation": {
            "platform": 4, "pageClickKey": "",
            "eid": "B2WSENAYGGNPHFXMEY2DOZGMS2ZRSPL6ZXMTXJNFMUWCS332YOBW5VI57MESBMUGURI76N2VRJWXMAM3E3CAZOAH5E",
            "fp": "6229eccbe60c067a7305af9933c093d4", "shshshfp": "fa9e1a0b9e6e3a515e846060de7fb43e",
            "shshshfpa": "fddc3a69-fcd3-f04f-67d2-5e8093fb29a2-1621210908",
            "shshshfpb": "d/tf8dOphtdkyBA4pRdJ6xw=="
        }
    })
    return result["data"]["floorInfoList"][0]['floorData']['shakingBoxInfo']['remainLotteryTimes']


def run():
    for cookies in jdCookie.get_cookies():
        print(cookies["pt_pin"])

        try:
            browseTask = template(cookies, "vvipclub_lotteryTask", {
                "info": "browseTask", "withItem": True})["data"][0]
            time.sleep(1)
            m = browseTask["totalPrizeTimes"] - browseTask["currentFinishTimes"]
            print("browseTask: ", m)
            if m > 0:
                _ids = [i["id"] for i in browseTask["taskItems"] if not i["finish"]]
                for item in _ids[::-1]:
                    print(template(cookies, "vvipclub_doTask", {"taskName": "browseTask", "taskItemId": item}))
                    time.sleep(1)
        except Exception as e:
            print('获取browseTask失败')
            traceback.print_exc()

        try:
            attentionTask = template(cookies, "vvipclub_lotteryTask", {
                "info": "attentionTask", "withItem": True})["data"][0]
            n = attentionTask["totalPrizeTimes"] - attentionTask["currentFinishTimes"]
            time.sleep(1)
            print("attentionTask: ", n)
            if n > 0:
                _ids = [i["id"] for i in attentionTask["taskItems"] if not i["finish"]]
                for i in range(n):
                    print(template(cookies, "vvipclub_doTask",
                                   {"taskName": "attentionTask", "taskItemId": str(_ids.pop())}))
                    time.sleep(2)
        except:
            print('获取attentionTask失败')
            traceback.print_exc()

        freeTimes = shake(cookies)
        print("freeTimes", freeTimes)
        for i in range(freeTimes):
            print(shark(cookies))
            time.sleep(1)
        time.sleep(1)
        print("\n\n")
        print("##" * 30)


if __name__ == "__main__":
    run()
