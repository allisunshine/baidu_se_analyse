# -*- coding = utf-8 -*-
# @Time : 2023/5/24 15:02
# @Author : maxiaoyun
# @File : dataHandle.py
# @Software : PyCharm

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import logging
import jieba
from collections import Counter
import string

# 创建日志记录器
logger = logging.getLogger(__name__)

# 创建引擎
engine = create_engine('mysql+mysqlconnector://buer:YDxzGDcJFsxaaecw@47.97.184.186:3306/buer')

# 创建会话
Session = sessionmaker(bind=engine)

# 定义数据模型
Base = declarative_base()


class BaiduSearch(Base):
    __tablename__ = 'baidu_search'
    id = Column(Integer, primary_key=True)
    page_number = Column(Integer)
    keyword = Column(String)
    search_word = Column(String)
    title = Column(String)
    current_url = Column(String)
    parent_url = Column(String)
    text_html = Column(String)
    create_time = Column(DateTime, default=datetime.now)


def save_webpage_to_db(data):
    session = Session()
    try:
        # 插入网页数据到数据库
        baiduSearch = BaiduSearch(page_number=data["page_number"],
                                  keyword=data['keyword'],
                                  search_word=data['search_word'],
                                  title=data['title'],
                                  current_url=data['current_url'],
                                  parent_url=data['parent_url'],
                                  text_html=data['text_html'])

        session.add(baiduSearch)
        session.commit()
    except Exception as e:
        # 发生异常时回滚事务
        session.rollback()
        logger.error(e)
    finally:
        session.close()


def queryBaike(word, page, pageSize):
    session = Session()
    try:
        offset = (page - 1) * pageSize  # 计算偏移量
        # 查询总条数
        total_count = session.query(func.count(BaiduSearch.id)).filter(
            BaiduSearch.search_word.like('%{}%'.format(word))).scalar()
        baikeData = session.query(BaiduSearch).filter(BaiduSearch.search_word.like('%{}%'.format(word))) \
            .limit(pageSize).offset(offset).all()
        results = []
        for data in baikeData:
            result = {
                'id': data.id,
                'page_number': data.page_number,
                'keyword': data.keyword,
                'search_word': data.search_word,
                'title': data.title,
                'current_url': data.current_url,
                'parent_url': data.parent_url,
                'text_html': data.text_html,
                'create_time': str(data.create_time)
            }
            results.append(result)
        return {'total_count': total_count, 'results': results}
    except Exception as e:
        logger.error(e)
    finally:
        session.close()


def queryAllBaike(word):
    session = Session()
    try:
        baikeData = session.query(BaiduSearch).filter(BaiduSearch.search_word.like('%{}%'.format(word))).all()
        results = []
        for data in baikeData:
            result = {
                'id': data.id,
                'page_number': data.page_number,
                'keyword': data.keyword,
                'search_word': data.search_word,
                'title': data.title,
                'current_url': data.current_url,
                'parent_url': data.parent_url,
                'text_html': data.text_html,
                'create_time': str(data.create_time)
            }
            results.append(result)
        return results
    except Exception as e:
        logger.error(e)
    finally:
        session.close()


def freqCount(word):
    results = queryAllBaike(word)
    titleStr = ''
    for data in results:
        title = data.get('title')
        if (title.endswith('_百度百科')):
            title = title[:-5]
        titleStr = ' '.join([titleStr, title])
    logger.info("titleStr:{}", titleStr)
    words = jieba.cut(titleStr)
    # 自定义停用词列表
    stop_words = [' ', '（', '）', '、', '的', '·', '百度', '百科', '：', '秒', '懂', '年', '中', '人', '与']
    words = [word for word in words if word not in stop_words and word not in string.punctuation]
    # 统计词频并取出前十个词
    word_count = Counter(words)
    top_ten_words = word_count.most_common(20)
    result_list = [{'word': word, 'count': count} for word, count in top_ten_words]
    return result_list


if __name__ == "__main__":
    queryBaike('', 1, 10)
