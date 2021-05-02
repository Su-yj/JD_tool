import jdCookie
import json
import requests
import time
import notification

"""
签到抽盲盒
https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html?has_native=0&source=huiyuan&utm_term=copyurl
"""


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


def getBeanTaskList(cookies, index=None):
    _beanTaskList = getTemplate(cookies, 'beanTaskList', {})
    if not index:
        return _beanTaskList['data']['taskInfos']
    return _beanTaskList['data']['taskInfos'][index]


def task_count(task):
    return task['maxTimes'] - task['times']


def takeTask(cookies):
    print('\n【签到】')
    _signBeanAct = getTemplate(cookies, 'signBeanAct', {})
    print(f"""signBeanAct: {_signBeanAct['data']}""")

    print('\n领好券')
    _queryCouponInfo = getTemplate(cookies, 'queryCouponInfo', {})
    if str(_queryCouponInfo['code']) == '0':
        print(f"""queryCouponInfo: {_queryCouponInfo['data']}""")
        if 'couponTaskInfo' in _queryCouponInfo['data']:
            for _ in range(task_count(_queryCouponInfo['data']['couponTaskInfo']['process'])):
                _sceneGetCoupon = getTemplate(cookies, 'sceneGetCoupon', {})
                print(_sceneGetCoupon)

    print('\n【京豆任务列表】')
    _taskInfos = getBeanTaskList(cookies)
    print(f"""_taskInfos: {_taskInfos}""")
    for index, item in enumerate(_taskInfos):
        print(f">>>{item['taskName']}")
        count = task_count(item)
        for _ in range(count):
            _task_infos = getBeanTaskList(cookies)
            temp = _task_infos[index]
            if temp['taskType'] == 8:
                time.sleep(1)
                _beanDoTask = getTemplate(cookies, 'beanDoTask',
                                          {"actionType": 1, "taskToken": temp['subTaskVOS'][0]['taskToken']})
                print(_beanDoTask)
                time.sleep(5)
            _beanDoTask = getTemplate(cookies, 'beanDoTask',
                                      {"actionType": 0, "taskToken": temp['subTaskVOS'][0]['taskToken']})
            print(_beanDoTask)
            time.sleep(0.5)

    print('\n【抽京豆】')
    _wheelSurfIndex = getTemplate(cookies, 'wheelSurfIndex', {"actId": "jgpqtzjhvaoym", "appSource": "jdhome"})
    print(_wheelSurfIndex)
    if str(_wheelSurfIndex.get('code')) == '0':
        _lotteryCount = _wheelSurfIndex.get('data', {}).get('lotteryCount', 0)
        _lotteryCode = _wheelSurfIndex.get('data', {}).get('lotteryCode', '')
        for _ in range(int(_lotteryCount)):
            _lotteryDraw = getTemplate(cookies, 'lotteryDraw', {"actId": "jgpqtzjhvaoym", "appSource": "jdhome",
                                                                "lotteryCode": _lotteryCode})
            print(_lotteryDraw)


def run():
    for cookies in jdCookie.get_cookies():
        takeTask(cookies)


if __name__ == '__main__':
    run()
