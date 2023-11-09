# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 19:55
# @Auther : Tiam
# @File : server
# @Project : DouyinSpider
import random
# pip install flask
from flask import Flask, request, jsonify
# pip install PyExecJS
import execjs
import urllib.parse

app = Flask(__name__)


# 这里Cookie指的一提的是msToken可以是随机107位大小写英文字母、数字生成的字符串; 参考: https://github.com/B1gM8c/X-Bogus
def generate_random_str(random_length=107):
    """
    根据传入长度产生随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
    length = len(base_str) - 1
    for _ in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


@app.route('/X-Bogus', methods=['POST'])
def generate_request_params():
    data = request.get_json()
    url = data.get('url')
    user_agent = data.get('user_agent')
    query = urllib.parse.urlparse(url).query
    xbogus = execjs.compile(open('./X-Bogus.js').read()).call('sign', query, user_agent)
    new_url = url + "&X-Bogus=" + xbogus
    response_data = {
        "param": new_url,
        "X-Bogus": xbogus,
        "msToken": generate_random_str(),
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787)
