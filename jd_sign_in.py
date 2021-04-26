import jdCookie
import json
import requests
import time
import notification

"""
签到抽盲盒
https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html?has_native=0&source=huiyuan&utm_term=copyurl
"""


def get_mune(cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'api.m.jd.com',
    }
    params = {
        'functionId': 'beanTaskList',
        'appid': 'ld',
    }
    url = 'https://api.m.jd.com/client.action'


def getTemplate(cookies, functionId='beanTaskList', body={}):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Host': 'api.m.jd.com',
    }
    params = (
        ('functionId', functionId),
        ('body', json.dumps(body)),
        ('appid', 'ld'),
    )

    response = requests.get('https://api.m.jd.com/client.action',
                            headers=headers, params=params, cookies=cookies)
    return response.json()


"""
{
    "code":"0",
    "data":{
        "taskInfos":[
            {
                "taskId":1,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/163192/9/7798/5516/6037526eE6df71306/1504fb66a0aa1a8e.png",
                "taskName":"双签领豆",
                "subTitleName":"最高领888京豆",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://m.jr.jd.com/integrate/signin/index.html?channel=qjdicon",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05130883-13816506-5601436297-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaR5jAOCGH83npInGk",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/163192/9/7798/5516/6037526eE6df71306/1504fb66a0aa1a8e.png",
                        "title":"双签领豆",
                        "subtitle":"最高领888京豆"
                    }
                ]
            },
            {
                "taskId":2,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/169647/2/7958/6111/60375235Ee8ca984a/9bfc9eb1bdc0cd93.png",
                "taskName":"种豆得豆",
                "subTitleName":"每周瓜分亿万京豆！",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://m.jd.com",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05130903-13816580-1401435676-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaS5jQMCGH83nlMkvw",
                        "comments":[
                            "openapp.jdmobile://virtual?params={"category":"jump","des":"jdreactcommon","modulename":"JDReactSowAndReap","appname":"JDReactSowAndReap","ishidden":true,"param":{"transparentenable":true,"source":"lingjingdourenwu"}}"
                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/169647/2/7958/6111/60375235Ee8ca984a/9bfc9eb1bdc0cd93.png",
                        "title":"种豆得豆",
                        "subtitle":"每周瓜分亿万京豆！"
                    }
                ]
            },
            {
                "taskId":4,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/163184/22/20762/16755/60851787E5b884535/5973df2ff2291c62.png",
                "taskName":"新客试借1元",
                "subTitleName":"得20元话费券",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://ms.jr.jd.com/jrpmobile/btbullion/bullion/jinTiaoIndex?sysCode=s02&sourceLink=c11",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05123401-14435688-1701483758-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaU5jQPCGH81X9NkCM",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/163184/22/20762/16755/60851787E5b884535/5973df2ff2291c62.png",
                        "title":"新客试借1元",
                        "subtitle":"得20元话费券"
                    }
                ]
            },
            {
                "taskId":5,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/162704/14/20751/3608/6085257eE5d19c772/407c0f84f4246251.png",
                "taskName":"精选床垫",
                "subTitleName":"直降3000",
                "taskType":3,
                "process":"4/4",
                "status":2,
                "score":"5",
                "times":4,
                "maxTimes":4,
                "subTaskVOS":[
                    {
                        "url":"https://pro.m.jd.com/mall/active/2c2beYYAEsDXWUSzexiQSwwDtQ3U/index.html",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05157605-14435994-0701480792-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaV5jUPCGH81XxNnKE",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/162704/14/20751/3608/6085257eE5d19c772/407c0f84f4246251.png",
                        "title":"精选床垫",
                        "subtitle":"直降3000"
                    }
                ]
            },
            {
                "taskId":6,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/164647/23/3823/5781/600a7ebfEa2106fb8/19686b3b280d1d9e.png",
                "taskName":"关注好店",
                "subTitleName":"关注指定店铺 立得",
                "taskType":1,
                "process":"5/5",
                "status":2,
                "score":"5",
                "times":5,
                "maxTimes":5,
                "subTaskVOS":[
                    {
                        "shopId":"1000004489",
                        "url":"1000004489",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05122945-14436289-6901464535-N#0-1-3--1042--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaW5jQICGD43XhOnVg",
                        "comments":[

                        ]
                    }
                ]
            },
            {
                "taskId":7,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/168821/29/3847/5227/600a7ecaE174ab2b3/0b254d2cc3b605db.png",
                "taskName":"猜你喜欢的商品",
                "subTitleName":"浏览5s 立得",
                "taskType":8,
                "process":"20/20",
                "status":2,
                "score":"5",
                "times":20,
                "maxTimes":20,
                "subTaskVOS":[
                    {
                        "skuId":"100020213940",
                        "status":2,
                        "mcInfo":"14629085-29456743-9206687348-100020213940#1-0-2--0--#1-tb-#3-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaX5jQICGD63X5LlkMwjA"
                    }
                ]
            },
            {
                "taskId":8,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/156035/11/7169/5032/600a7eddE7031e06d/965f0d7d9e2de7a2.png",
                "taskName":"惊喜福利",
                "subTitleName":"去看看好玩的 立得",
                "taskType":3,
                "process":"2/2",
                "status":2,
                "score":"5",
                "times":2,
                "maxTimes":2,
                "subTaskVOS":[
                    {
                        "url":"https://lottery.m.jd.com/#/home",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05180819-14401291-6401459065-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaY5jMMCGH82HVKk4I",
                        "comments":[

                        ],
                        "icon":"",
                        "title":"惊喜福利",
                        "subtitle":""
                    }
                ]
            },
            {
                "taskId":9,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/153153/27/17423/6266/601d25ddE63778b5c/140189ad7a5954a5.png",
                "taskName":"边玩边赚",
                "subTitleName":"送你京豆和现金",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://funearth.m.jd.com/babelDiy/Zeus/3BB1rymVZUo4XmicATEUSDUgHZND/index.html?source=6",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05218303-14166736-1201451215-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaZ5jQKCGH82H1IlC0",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/153153/27/17423/6266/601d25ddE63778b5c/140189ad7a5954a5.png",
                        "title":"边玩边赚",
                        "subtitle":"送你京豆和现金"
                    }
                ]
            },
            {
                "taskId":10,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/151090/12/18685/5988/601d256aEc57a5b4e/0fcd6df64b1bb725.png",
                "taskName":"下单返京豆",
                "subTitleName":"马上去领取",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://jddx.jd.com/m/money/rebate/index.html?bizline=22&bizsource=jdgwfjd",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05218301-14166731-1701456809-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaRzR4JD2D52XlMnRp5",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/151090/12/18685/5988/601d256aEc57a5b4e/0fcd6df64b1bb725.png",
                        "title":"下单返京豆",
                        "subtitle":"马上去领取"
                    }
                ]
            },
            {
                "taskId":11,
                "icon":"https://m.360buyimg.com/babel/jfs/t1/151330/17/20099/6297/6035e6aaE467907d4/73447b20e088b840.png",
                "taskName":"兑权益",
                "subTitleName":"京豆兑好礼",
                "taskType":3,
                "process":"1/1",
                "status":2,
                "score":"5",
                "times":1,
                "maxTimes":1,
                "subTaskVOS":[
                    {
                        "url":"https://jdmall.m.jd.com/",
                        "copy1":"",
                        "copy2":"",
                        "copy3":"",
                        "status":2,
                        "mcInfo":"05239300-14245005-1501455873-M#0-2-1--0--#1-tb-#1-#jdinteractive",
                        "taskToken":"P15tv92SB4Z81TfT0cCjVVnoaRzB4JDWD52XlPnTY6",
                        "comments":[

                        ],
                        "icon":"https://m.360buyimg.com/babel/jfs/t1/151330/17/20099/6297/6035e6aaE467907d4/73447b20e088b840.png",
                        "title":"兑权益",
                        "subtitle":"京豆兑好礼"
                    }
                ]
            }
        ],
        "taskTopIcon":"https://m.360buyimg.com/babel/jfs/t1/158840/34/4789/42807/600eb102Eaf58554d/97a6cbbfc3ee3933.png"
    }
}
"""
