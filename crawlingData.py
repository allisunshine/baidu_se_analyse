# -*- coding = utf-8 -*-
# @Time : 2023/5/24 15:14
# @Author : maxiaoyun
# @File : crawlingData.py
# @Software : PyCharm
import ssl
import urllib.request
import urllib
from lxml import etree
import requests

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# baseUrl = "https://baike.baidu.com/item/Python"
baseUrl = "https://baike.baidu.com/item/Python/407313"


# 爬取数据
def getData(baseUrl):
    dataList = []
    html = askUrl(baseUrl)

    # return dataList


def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": 'zhishiTopicRequestTime=1684916963268; BAIKE_SHITONG=%7B%22data%22%3A%22e1258462535cb0c3754c1c07d04bd7efe2ec35671a6628040ea5af4c2624d36e94283d67e2e31b225a4505d37cadb126316a79316ee20383637420529523cb41c5d1a45ea7d1f0011a82dad7588882dd131ab3bec01e8f5f39d44f72bbd95188%22%2C%22key_id%22%3A%2210%22%2C%22sign%22%3A%227a83ca1e%22%7D; BAIDUID_BFESS=EC87C7F7415104353F4EE5721E221A35:FG=1; __bid_n=186ab7b140a6191d394207; BDUSS=lHbmtZSlBTY2VpT3NWdGZveVBzMDF5dWttb0NMbjk2N3Y1OVI3V0cybUd-ekJrSVFBQUFBJCQAAAAAAAAAAAEAAADgtmg9vL7Hs8rmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZyCWSGcglkU3; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04331163600KZL7BHS3svXNCEwoSryXnX3giiwKP3Pbk7LrI%2BFi3SbBoyVgqoQhkKjK9k57WU0rC%2BJU3rXa7OESUlGk9zWji6tLb7KDGMG7Zk1KqN%2F8fpObAHU%2BCYxhfxzV03S0ALzT1fP6Til7Q7X%2BCyTY2zqSi1CbIKxW%2FOfsZXWk%2FOX9BkpxZFDHunaO%2Bh4KHaPwSF4X6HkdSB7d40CWclNSgHJzcEAdleCg3sdeTyYJFsgWc6C%2FUoUtpTzWc%2BK0jQy0y6tcSVPqDevqAG2OPlvy0GeJIZ5lFM486pjvaH6GPIDeF3M%3D21584088085358070091940004476911; BDUSS_BFESS=lHbmtZSlBTY2VpT3NWdGZveVBzMDF5dWttb0NMbjk2N3Y1OVI3V0cybUd-ekJrSVFBQUFBJCQAAAAAAAAAAAEAAADgtmg9vL7Hs8rmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZyCWSGcglkU3; BIDUPSID=EC87C7F7415104353F4EE5721E221A35; PSTM=1683114286; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1684609143; H_PS_PSSID=38516_36549_38540_38618_38538_38593_38596_38486_38414_38635_38506_26350_38569_38622_38658; ZFY=Vhh24F1cmbkfKTUBfpNzQ:AlJR1m3I5d31PHB9RblAmE:C; BA_HECTOR=a0ak802k8kal8h25ag0galc51i6qtkb1m; PSINO=5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; FPTOKEN=/qYwhIeGN0Xqjb/0liTOD9rsaaeK46QSgYFlHzCHXdwwwaiphGQrhlZmRO2G1Q5RZMLW3+5q8Igpic9FgiRw+d+ESjK3IIg3wQh5tdCsLtw3dR0MVJoTK9YN5vOjcD4lLSo32HG+yDglTG6e7ftbs5fqgPZoe1ag30pYzc0vPFIof8fpcEfy+TUCuyKj8HgT1wcgpO3BHh+ZFUsnmPzRyxRt6nW1Y6Aot2FGhvoMplBb1SDm5DBn5cULAcBJeeybsXAklETMraFEjqyCV/X1oCCY1UohslO3rWViVH8Q3WMXy3tMXdcnnCml2WsGkDdn5JzRICAvUsfvhSgWobpPoJohSGFoKQRrOPW28IYkIFibu/eVIAeZKfhGNIVaqGoDRZGUO35IyJg5OIJyhYMjUw==|PuBhqKRLeF40UtbYIZ33ssIJYP/HXzbesXdYGfzggdU=|10|8917c699a6292c963aa09be7393f1bc9; zhishiTopicRequestTime=1684913111803; BK_SEARCHLOG=%7B%22key%22%3A%5B%22112%22%2C%22%E2%80%9C%E5%B7%85%E5%B3%B0%E4%BD%BF%E5%91%BD%E2%80%9D%E7%8F%A0%E5%B3%B0%E7%A7%91%E8%80%83%22%2C%22python%22%2C%22%E5%8D%81%E5%85%AB%E7%B1%BD%22%5D%7D; X_ST_FLOW=0; baikeVisitId=48075135-2386-456d-9bc9-491ce2e90ce7; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1684917159; ab_sr=1.0.1_MTNlZWM2ZGZlYjdhYTIxOTY0MzU4NmQ3ZGEwZmIwYThiODI3OTVhYjY3YjQ0MzI4MDc2ODFiMTJlZDM1ZmRhNzliYTg4MWIxYzUzYzEyYjM1YmQ4MDVhZGJhMTg5YmMyYzJlNDQ0YjNjNTI5MmM5YWQwNzQ0MTI1MmI0NDgzMDg4YjA0YjdhMGRhNzMzYWYxZWE3ZGI2Mjg1MWY2NjZmY2ExNDAyYTZkYWUxNTFlYjE2OTcwZDk5OWIzYjkwMmVh; RT="z=1&dm=baidu.com&si=25eefe04-b373-4078-b741-f289930ad903&ss=li1byd5a&sl=s&tt=7p4t&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4837d&ul=487gn"'
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        # response = urllib.request.urlopen(request)
        response = requests.get(url, headers=head)
        html = response.content.decode('utf-8')
        # html = response.read().decode('utf-8')
        print(html)
    except Exception as e:
        print(e)
    return html


if __name__ == "__main__":
    askUrl(baseUrl)
