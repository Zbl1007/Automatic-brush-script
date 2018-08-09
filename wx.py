#coding:utf-8
#!/usr/bin/env python

# 功能：自动接单！
# 平台：微信，金锦耀世环球平台

# 作者：Zbl
# 邮箱：1399853961@qq.com
# 使用注意事项: 需要每天手动修改2 个headers中“x-rn-access-token”后的值( 通过抓包而来 即cookie值 )
#         第一次使用请改headers中"x-rn-platform"和"x-rn-user-id"的值

import requests
import json
import sys
import re
import os

requests = requests.Session()


def ss(Type):

    #每天手动更改，抓包所得
    cookie = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ0eXBlXCI6MyxcInVzZXJOYW1lXCI6XCJCMjkwM-W8oOeZveS6rlwiLFwicm9sZXNcIjpbe1wiaWRcIjo1Nzk0OCxcInZlcnNpb25cIjowLFwiY3JlYXRlQXRcIjpcIjIwMTgtMDgtMDMgMTk6MDI6MzdcIixcInVzZXJJZFwiOjU4NzU0LFwicm9sZUlkXCI6MzAxLFwicm9sZU5hbWVcIjpcIua0vuWFi-euoeeQhuWRmFwifV0sXCJ1c2VySWRcIjo1ODc1NCxcInBsYXRmb3JtXCI6MyxcIm1vYmlsZVwiOlwiMTc2NzQ3MTQxODZcIixcInN0YXR1c1wiOjIsXCJ3b3JraW5nRmxhZ1wiOjF9IiwiaXNzIjoicnVvbmFuIiwiZXhwIjoxNTMzODAxMDQxLCJpYXQiOjE1MzM3ODMwNDB9.mq4DKTMRw6EtM_VLN4PO9Qlx4j1DxcUvEG7SW71vtgo"
    
    headers = {
        "Host": "api.changjiang1688.com:8080",
        "Origin": "http://m.changjiang1688.com",
        "x-rn-access-token": cookie,
        # "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; ONEPLUS A5000 Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044203 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/en",
        # "Accept": "*/*",

        #下面的这个2个改成自己的
        "x-rn-platform": "3",
        "x-rn-user-id": "58754",
            
        # "Referer": "http://m.changjiang1688.com/workerIndex?sessionKey=worker_session_oitjM0W78QjXqguO39xTnIDGQK8YeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ0eXBlXCI6MyxcInVzZXJOYW1lXCI6XCJCMjkwM-W8oOeZveS6rlwiLFwicm9sZXNcIjpbe1wiaWRcIjo1Nzk0OCxcInZlcnNpb25cIjowLFwiY3JlYXRlQXRcIjpcIjIwMTgtMDgtMDMgMTk6MDI6MzdcIixcInVzZXJJZFwiOjU4NzU0LFwicm9sZUlkXCI6MzAxLFwicm9sZU5hbWVcIjpcIua0vuWFi-euoeeQhuWRmFwifV0sXCJ1c2VySWRcIjo1ODc1NCxcInBsYXRmb3JtXCI6MyxcIm1vYmlsZVwiOlwiMTc2NzQ3MTQxODZcIixcInN0YXR1c1wiOjIsXCJ3b3JraW5nRmxhZ1wiOjF9IiwiaXNzIjoicnVvbmFuIiwiZXhwIjoxNTMzNjIxMDM4LCJpYXQiOjE1MzM2MDMwMzd9.g96KO7DFWHtWT-565rXdjK5y7YthjXd9qBPQBrtbAoA&t=1533603037057",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "en,en-US;q=0.8,zh-CN;q=0.6",
        # "X-Requested-With": "com.tencent.mm"

    }
    if(Type==2):
        url = "http://api.changjiang1688.com:8080/task/list_plan_4_flow?pageNum=1&type=2&pageSize=10&keyLike=&completeFlag=0&cancelFlag=0"
        url1 = "http://api.changjiang1688.com:8080/task/accept_task_4_flow"
    else:
        url1 = "http://api.changjiang1688.com:8080/task/accept_task"
        url = "http://api.changjiang1688.com:8080/task/list_plan?pageNum=1&type="+str(Type)+"&pageSize=10&keyLike=&completeFlag=0&cancelFlag=0"
    


    response = requests.get(url,headers=headers)
    data = str(response.content,encoding='utf-8')
    print(data)
    result = json.loads(data)
    if(result['data']):
        headers = {
            "Host": "api.changjiang1688.com:8080",
            "Content-Length": "8",
            "Origin": "http://m.changjiang1688.com",
            "x-rn-access-token": cookie,
            #头改不改随意
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; ONEPLUS A5000 Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044203 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/en",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",

            #下面的这个2个改成自己的
            "x-rn-platform": "3",
            "x-rn-user-id": "58754",

            # "Referer": "http://m.changjiang1688.com/workerIndex?sessionKey=worker_session_oitjM0W78QjXqguO39xTnIDGQK8YeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ0eXBlXCI6MyxcInVzZXJOYW1lXCI6XCJCMjkwM-W8oOeZveS6rlwiLFwicm9sZXNcIjpbe1wiaWRcIjo1Nzk0OCxcInZlcnNpb25cIjowLFwiY3JlYXRlQXRcIjpcIjIwMTgtMDgtMDMgMTk6MDI6MzdcIixcInVzZXJJZFwiOjU4NzU0LFwicm9sZUlkXCI6MzAxLFwicm9sZU5hbWVcIjpcIua0vuWFi-euoeeQhuWRmFwifV0sXCJ1c2VySWRcIjo1ODc1NCxcInBsYXRmb3JtXCI6MyxcIm1vYmlsZVwiOlwiMTc2NzQ3MTQxODZcIixcInN0YXR1c1wiOjIsXCJ3b3JraW5nRmxhZ1wiOjF9IiwiaXNzIjoicnVvbmFuIiwiZXhwIjoxNTMzNjIxMDM4LCJpYXQiOjE1MzM2MDMwMzd9.g96KO7DFWHtWT-565rXdjK5y7YthjXd9qBPQBrtbAoA&t=1533603037057",
            # "Accept-Encoding": "gzip, deflate",
            # "Accept-Language": "en,en-US;q=0.8,zh-CN;q=0.6",
            # "X-Requested-With": "com.tencent.mm"
        }
        print(result['data']['list'])
        for i in result['data']['list']:
            ID = str(i['id'])
            response = requests.post(url1,data = ID,headers=headers)
            print(response.text)
        return 1;
    print(1)
