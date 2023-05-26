# -*- coding = utf-8 -*-
# @Time : 2023/5/24 15:02
# @Author : maxiaoyun
# @File : dataHandle.py
# @Software : PyCharm

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 创建引擎
engine = create_engine('mysql+mysqlconnector://root@127.0.0.1:3306/python_project')

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BaiduSearch(Base):
    __tablename__ = 'baidu_search'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    current_url = Column(String)
    parent_url = Column(String)
    original_html = Column(String)
    text_html = Column(String)
    create_time = Column(DateTime, default=datetime.now)
