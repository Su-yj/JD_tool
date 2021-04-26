import jdCookie
import json
import requests
import time
import notification


BODY_LIST = [
    {'type': '3', "source": "home", "awardFlag": False, 'itemId': 'zddd'},  # 种豆得豆
    {'type': '4_2001383800', "source": "home", "awardFlag": False, 'itemId': '2001383800'},  # 双签领豆
    {'type': '4_2001383802', "source": "home", "awardFlag": False, 'itemId': '2001383802'},  # 抽京豆
    {'type': '4_2001383803', "source": "home", "awardFlag": False, 'itemId': '2001383803'},  # 摇京豆
    {'type': '4_2001383801', "source": "home", "awardFlag": False, 'itemId': '2001383801'},  # 进店领豆
    {"source": "home", "awardFlag": True},  # 领取奖励
]


def getTemplate(cookies, functionId, body):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'api.m.jd.com',
    }
    params = (
        ('functionId', functionId),
        ('body', json.dumps(body)),
        ('appid', 'ld'),
    )

    response = requests.get('https://api.m.jd.com/client.action', headers=headers, params=params, cookies=cookies)
    return response.json()


def takeTask(cookies):
    for body in BODY_LIST:
        j = getTemplate(cookies, 'beanHomeTask', body)
        print(j)
        time.sleep(1)


def run():
    for cookies in jdCookie.get_cookies():
        takeTask(cookies)


if __name__ == '__main__':
    run()
