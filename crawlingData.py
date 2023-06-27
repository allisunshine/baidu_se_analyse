# -*- coding = utf-8 -*-
# @Time : 2023/5/24 15:14
# @Author : maxiaoyun
# @File : crawlingData.py
# @Software : PyCharm
import ssl
from bs4 import BeautifulSoup
import requests
import json
import codecs

import dataHandle

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

baseUrl = "https://baike.baidu.com/item/"


def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": 'zhishiTopicRequestTime=1687596589216; BAIKE_SHITONG=%7B%22data%22%3A%22a52791141b1587158d91e84f72f4a9d7c8d1d3ee925eecfc388a0c8c412913670439c75e0ab69ea05d02b34446c06d241e40b4bef612c80786a63c4d5f45647191e335741d528e597507301068b1ef12169aa270d99fb99b41f856832075da78%22%2C%22key_id%22%3A%2210%22%2C%22sign%22%3A%2205747ff0%22%7D; BAIDUID_BFESS=EC87C7F7415104353F4EE5721E221A35:FG=1; __bid_n=186ab7b140a6191d394207; BDUSS=lHbmtZSlBTY2VpT3NWdGZveVBzMDF5dWttb0NMbjk2N3Y1OVI3V0cybUd-ekJrSVFBQUFBJCQAAAAAAAAAAAEAAADgtmg9vL7Hs8rmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZyCWSGcglkU3; BDUSS_BFESS=lHbmtZSlBTY2VpT3NWdGZveVBzMDF5dWttb0NMbjk2N3Y1OVI3V0cybUd-ekJrSVFBQUFBJCQAAAAAAAAAAAEAAADgtmg9vL7Hs8rmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZyCWSGcglkU3; BIDUPSID=EC87C7F7415104353F4EE5721E221A35; PSTM=1683114286; ZFY=Vhh24F1cmbkfKTUBfpNzQ:AlJR1m3I5d31PHB9RblAmE:C; FPTOKEN=o4bJuVDO0iSEpVraouwOp8RyBfv6ymjfqokTyApFsHDYw7KJCWlnwUxW4PL6eFgPfP/QkDTcTGPlLLQa+tG31smyZu5U0CdbsxjgOMrVwXIfPqEkuv6fuKdVQO08qlxBlRzFQT4El+nt+XoFMHBgnfiWZoZeA3bzfI60I9dSk9dpR3WjeCra0tdRDP76foSA4KqaYsHGZDKTUrwltDlcZJS6WVAI3FWixQHwb/dXDrrtJHNESZfTvMZ3KRCDTwprT+9M7NdjZYys2Q+9s4sQ5a6G5KXa4X49xc6npWRjACM0XsxQ4QATwczn+mgDJY6KI/LTgVxXsR0HwsR5g/kwOilywWf2Gb+OahptrYUgCmHJ7ifft4oAOJzHnvo6JtlAeAoVCY4Gs6N2yPqhNULL7g==|sOc2RFOMUuoroQQiLQQoqCkHbtTHMnxM1INQwCFqwak=|10|7e5960457f7f5a0f8142513f56418b25; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1686480232,1687314699; BK_SEARCHLOG=%7B%22key%22%3A%5B%22Python%22%2C%22python%22%2C%22112%22%2C%22%E2%80%9C%E5%B7%85%E5%B3%B0%E4%BD%BF%E5%91%BD%E2%80%9D%E7%8F%A0%E5%B3%B0%E7%A7%91%E8%80%83%22%2C%22%E5%8D%81%E5%85%AB%E7%B1%BD%22%5D%7D; baikeVisitId=38310932-fc01-4bd5-a068-32b1b3f89fa6; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1687596592; RT="z=1&dm=baidu.com&si=0bbfe14e-16bb-4af3-b398-bd3ce98f8e39&ss=lj9qnplg&sl=l&tt=z5i&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=sgj6&ul=5582a"',
        # "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'zh-CN,zh;q=0.9',
        "Cache-Control": 'max-age=0',
        "Connection": 'keep-alive',
        "Host": 'baike.baidu.com',
        "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "Sec-Ch-Ua-Mobile": '?0',
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": 'document',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-Site": 'none',
        "Sec-Fetch-User": '?1',
        "Upgrade-Insecure-Requests": '1'
    }

    session = requests.Session()
    session.headers.update(head)

    # 发送初始请求，提取重定向链接
    response = session.get(url, allow_redirects=True)
    redirect_url = response.url
    print("重定向后的URL:", redirect_url)

    # if redirect_url:
    #     # 设置重定向链接为Session的基础URL
    #     session.base_url = redirect_url

    # 发送请求，自动处理重定向
    # response = session.get(keyword)
    # response = session.get(url, verify=False)
    # response = requests.get(url, headers=head,verify=False)
    # text = response.read().decode('utf-8')
    return response


def crawl_baidu_baike(word, max_pages):
    visited_urls = set()
    keyword = word
    queue = [(1, keyword, '')]  # (网页编号, 当前关键词, 父链接)

    while len(visited_urls) < max_pages and queue:
        page_number, keyword, parent_url = queue.pop(0)
        url = baseUrl + keyword

        if url in visited_urls:
            continue

        visited_urls.add(url)
        response = askUrl(url)
        # response.encoding = 'utf-8'

        if response.status_code == 200:
            originalHtml = response.text
            # originalHtml = response.text
            soup = BeautifulSoup(originalHtml, 'html.parser')
            title = soup.find('title').text.strip()
            contentText = soup.get_text(strip=True)
            div_tag = soup.find('div', class_='lemma-summary J-summary')
            if div_tag is not None:
                mainContentText = div_tag.get_text(strip=True)
            else:
                mainContentText = contentText
            # 构造网页数据
            data = {
                'page_number': page_number,
                'keyword': keyword,
                'search_word': word.split('/')[0],
                'title': title,
                'current_url': url,
                'parent_url': parent_url,
                'text_html': mainContentText
            }

            # 保存网页数据到数据库
            dataHandle.save_webpage_to_db(data)
            fileName = 'baikeDetail/' + word.split('/')[0] + '_' + str(page_number) + '_json.txt'
            fileData = {
                'page_number': page_number,
                'title': title,
                'current_url': url,
                'parent_url': parent_url,
                'original_html': originalHtml,
                'text_html': contentText
            }
            fileJsonData = json.dumps(fileData, indent=4, ensure_ascii=False)
            # 写文件
            with codecs.open(fileName, "w", encoding="utf-8") as file:
                file.write(fileJsonData)
            # 输出当前处理的网页信息
            print(f'Crawled page {page_number}: {url}')

            # 提取该网页中的关联词条，并加入待爬取队列
            links = soup.find_all('a', href=True)
            queueNum = page_number
            for link in links:
                href = link['href']
                if href.startswith('/item/'):
                    next_keyword = href[6:]
                    queueNum += 1
                    queue.append((queueNum, next_keyword, url))
        else:
            print(f'Failed to crawl page {page_number}: {url}')


if __name__ == "__main__":
    crawl_baidu_baike("python/407313", 500)
