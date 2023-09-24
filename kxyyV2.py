# -*- coding: utf-8 -*-
# k小阅阅阅读多线程V2.0
# Author: kk
# date：2023/9/24
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
小阅阅阅读入口：https://wi83860.aiskill.top:10251/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi83860.aiskill.top:10251&codeuserid=2&time=1695092177
阅读文章抓出ysm_uid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export xyyck="[{'name':'xxx','ysmuid':'xxx'},{'name':'xxx','ysmuid':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import datetime
from io import StringIO
import threading
import ast
import json
import os
import random
import re
from queue import Queue
import requests

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time
from urllib.parse import urlparse, parse_qs

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 8000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

qwbotkey = os.getenv('qwbotkey')
xyyck = os.getenv('xyyck')
if not qwbotkey or not xyyck:
    print('请仔细阅读上方注释并设置好key和ck')
    exit()

checklist = ['MzkxNTE3MzQ4MQ==', 'Mzg5MjM0MDEwNw==', 'MzUzODY4NzE2OQ==', 'MzkyMjE3MzYxMg==',
             'MzkxNjMwNDIzOA==', 'Mzg3NzUxMjc5Mg==', 'Mzg4NTcwODE1NA==', 'Mzk0ODIxODE4OQ==',
             'Mzg2NjUyMjI1NA==', 'MzIzMDczODg4Mw==', 'Mzg5ODUyMzYzMQ==', 'MzU0NzI5Mjc4OQ==',
             'Mzg5MDgxODAzMg==']


def ftime():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def debugger(text):
    if debug:
        print(text)


def printlog(text):
    if printf:
        print(text)


def send(msg, title='通知', url=None):
    if not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",
                # "mentioned_list": ["@all"],
            }
        }
    else:
        data = {"msgtype": "news",
                "news": {"articles":
                             [{"title": title, "description": msg, "url": url,
                               "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'
                               }]}}
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'
    resp = requests.post(whurl, data=json.dumps(data)).json()
    if resp.get('errcode') != 0:
        print('消息发送失败，请检查key和发送格式')
        return False
    return resp


def getmpinfo(link):
    if not link or link == '':
        return False
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}
    res = requests.get(link, headers=headers)
    html = etree.HTML(res.text)
    # print(res.text)
    title = html.xpath('//meta[@*="og:title"]/@content')
    if title:
        title = title[0]
    url = html.xpath('//meta[@*="og:url"]/@content')
    if url:
        url = url[0].encode().decode()
    biz = re.findall(r'biz=(.*?)&', link) or re.findall(r'biz=(.*?)&', url)
    if biz:
        biz = biz[0]
    username = html.xpath('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')
    if username:
        username = username[0].strip()
    id = re.findall(r"user_name.DATA'\) : '(.*?)'", res.text) or html.xpath(
        '//span[@class="profile_meta_value"]/text()')
    if id:
        id = id[0]
    ctt = re.findall(r'createTime = \'(.*)\'', res.text)
    if ctt:
        ctt = ctt[0][5:]
    text = f'{ctt}|{title}|{biz}|{username}|{id}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


def ts():
    return str(int(time.time())) + '000'


class XYY:
    def __init__(self, cg):
        self.name = cg['name']
        self.ysm_uid = None
        self.ysmuid = cg.get('ysmuid')
        self.sec = requests.session()
        self.sec.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'ysmuid={self.ysmuid};',
        }
        self.msg = ''

    def init(self):
        """获取阅读任务必须的ysm_uid"""
        if not self.ysmuid:
            print('ck没有ysmuid，不能运行本脚本，自动退出')
            return False
        i = 0
        while i < 5:
            res = self.sec.get('http://1695480664.snak.top/').text
            self.ysm_uid = re.findall(r'unionid="(o.*?)";', res)
            if self.ysm_uid:
                self.ysm_uid = self.ysm_uid[0]
                href = re.findall(r'href="(.*?)">提现', res)
                if href:
                    href = href[0]
                    qs = parse_qs(urlparse(href).query)
                    self.unionid = qs.get('unionid')[0]
                    self.request_id = qs.get('request_id')[0]
                    self.netloc = urlparse(href).netloc
                else:
                    printlog(f'{self.name} 获取提现参数失败，本次不提现')
                    self.msg += f'获取提现参数失败，本次不提现\n'
                return True
            else:
                i += 1
                continue
        printlog(f'{self.name} 获取ysm_uid失败，请检查账号有效性')
        self.msg += '获取ysm_uid失败，请检查账号有效性\n'
        return False

    def user_info(self):
        url = f'http://1695492718.snak.top/yunonline/v1/gold?unionid={self.ysm_uid}&time={ts()}'
        res = self.sec.get(url).json()
        debugger(f'userinfo {res}')
        data = res.get("data")
        self.last_gold = res.get("data").get("last_gold")
        remain_read = data.get("remain_read")
        msg = f'今日已经阅读了{data.get("day_read")}篇文章,剩余{remain_read}未阅读，今日获取金币{data.get("day_gold")}，剩余{self.last_gold}'
        printlog(f'{self.name}:{msg}')
        self.msg += (msg + '\n')
        if remain_read == 0:
            return False
        return True

    def getKey(self):
        url = 'http://1695492718.snak.top/yunonline/v1/wtmpdomain'
        data = f'unionid={self.ysm_uid}'
        res = self.sec.post(url, data=data).json()
        debugger(f'getkey {res}')
        domain = res.get('data').get('domain')
        self.uk = parse_qs(urlparse(domain).query).get('uk')[0]
        host = urlparse(domain).netloc
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Origin': f'https://{host}',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }

    def read(self):
        time.sleep(3)
        params = {'uk': self.uk}
        while True:
            url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'
            res = requests.get(url, headers=self.headers, params=params)
            self.msg += ('-' * 50 + '\n')
            debugger(f'read1 {res.text}')
            res = res.json()
            if res.get('errcode') == 0:
                link = res.get('data').get('link')
                wxlink = self.jump(link)
                if 'mp.weixin' in wxlink:
                    mpinfo = getmpinfo(wxlink)
                    biz = mpinfo['biz']
                    self.msg += ('开始阅读 ' + mpinfo['text'] + '\n')
                    printlog(f'{self.name}:开始阅读 ' + mpinfo['text'])
                    if biz in checklist:
                        send(msg=f"{mpinfo['text']}", title=f'{self.name} 小阅阅阅读过检测', url=wxlink)
                        self.msg += '遇到检测文章，已发送到微信，手动阅读，暂停50秒\n'
                        printlog(f'{self.name}:遇到检测文章，已发送到微信，手动阅读，暂停50秒')
                        time.sleep(50)
                else:
                    self.msg += f'{self.name} 小阅阅跳转到 {wxlink}\n'
                    printlog(f'{self.name}: 小阅阅跳转到 {wxlink}')
                    continue
                tsm = random.randint(7, 10)
                self.msg += f'本次模拟读{tsm}秒\n'
                time.sleep(tsm)
                url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={self.uk}&time={tsm}&timestamp={ts()}'
                requests.get(url, headers=self.headers)
            elif res.get('errcode') == 405:
                printlog(f'{self.name}:阅读重复')
                self.msg += '阅读重复\n'
                time.sleep(1.5)
            elif res.get('errcode') == 407:
                printlog(f'{self.name}:{res.get("msg")}')
                self.msg += (res.get('msg') + '\n')
                return True
            else:
                printlog(f'{self.name}:{res.get("msg")}')
                self.msg += (res.get("msg") + '\n')
                time.sleep(1.5)

    def jump(self, link):
        host = urlparse(link).netloc
        headers = {
            'Host': host,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Cookie': f'ysmuid={self.ysmuid}',
        }
        res = requests.get(link, headers=headers, allow_redirects=False)
        Location = res.headers.get('Location')
        return Location

    def withdraw(self):
        if not self.unionid:
            return False
        if int(self.last_gold) < txbz:
            printlog(f'{self.name} 没有达到你设置的提现标准{txbz}')
            self.msg += f'没有达到你设置的提现标准{txbz}\n'
            return False
        gold = int(int(self.last_gold) / 1000) * 1000
        self.msg += f'本次提现金币{gold}\n'
        printlog(f'{self.name}:本次提现金币{gold}')
        # self.sec.headers.update({'referer': f'{href}', 'origin': f'http://{netloc}'})
        if gold:
            url = f'http://{self.netloc}/yunonline/v1/user_gold'
            printlog(url)
            data = f'unionid={self.unionid}&request_id={self.request_id}&gold={gold}'
            res = self.sec.post(url, data=data)
            debugger(f'gold {res.text}')
            url = f'http://{self.netloc}/yunonline/v1/withdraw'
            data = f'unionid={self.unionid}&signid={self.request_id}&ua=0&ptype=0&paccount=&pname='
            res = self.sec.post(url, data=data)
            debugger(f'withdraw {res.text}')
            self.msg += f"提现结果 {res.json()['msg']}"
            printlog(f'{self.name}:提现结果 {res.json()["msg"]}')

    def run(self):
        self.msg += ('=' * 50 + f'\n账号：{self.name}开始任务\n')
        printlog(f'账号：{self.name}开始任务')
        if not self.init():
            return False
        if self.user_info():
            self.getKey()
            self.read()
            self.user_info()
            time.sleep(0.5)
        self.withdraw()
        printlog(f'账号：{self.name} 本轮任务结束')
        if not printf:
            print(self.msg)


def yd(q):
    while not q.empty():
        ck = q.get()
        api = XYY(ck)
        api.run()


def get_ver():
    ver = 'kxyyV2 V2.0.1'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    res = requests.get('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json', headers=headers).json()
    v1 = ver.split(' ')[1]
    v2 = res.get('version').get(ver.split(' ')[0])
    msg = f"当前版本 {v1}，仓库版本 {v2}"
    if v1 < v2:
        msg += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'
    return msg


if __name__ == '__main__':
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)
    try:
        xyyck = ast.literal_eval(xyyck)
    except:
        pass
    threads = []
    q = Queue()
    for i in xyyck:
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(20)  # 设置并发延迟
    for thread in threads:
        thread.join()