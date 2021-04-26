import jdCookie
import json
import requests
import time
import notification


BODY_LIST = [
    {'type': '3', "source": "home", "awardFlag": False, 'itemId': 'zddd'},  # 种豆得豆
    {'type': '4_2001383800', "source": "home",
        "awardFlag": False, 'itemId': '2001383800'},  # 双签领豆
    {'type': '4_2001383802', "source": "home",
        "awardFlag": False, 'itemId': '2001383802'},  # 抽京豆
    {'type': '4_2001383803', "source": "home",
        "awardFlag": False, 'itemId': '2001383803'},  # 摇京豆
    {'type': '4_2001383801', "source": "home",
        "awardFlag": False, 'itemId': '2001383801'},  # 进店领豆
    {"source": "home", "awardFlag": True},  # 领取奖励
]


def get_params(body):
    return {
        'functionId': 'beanHomeTask',
        'body': body,
        'appid': 'ld',
        'client': 'apple',
        'clientVersion': 'null',
        'networkType': 'null',
        'osVersion': '13.2.3',
        'uuid': 'null',
        'openudid': 'null',
        'jsonp': f'jsonp_{int(time.time() * 1000)}_81220',
    }


def done(cookies):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'referer': 'https://h5.m.jd.com/',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }
    for body in BODY_LIST:
        params = get_params(json.dumps(body))
        requests.get('https://api.m.jd.com/client.action',
                     params=params, headers=headers)


def run():
    for cookies in jdCookie.get_cookies():
        done(cookies)


if __name__ == '__main__':
    run()
