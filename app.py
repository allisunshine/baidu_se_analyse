from flask import Flask
import crawlingData
import dataHandle

app = Flask(__name__)


@app.route('/crawlingBaiduData/<word>')
def hello_world(word):  # put application's code here
    # 爬取数据逻辑

    return '爬取数据:%s'%(word)




if __name__ == '__main__':
    app.run()
