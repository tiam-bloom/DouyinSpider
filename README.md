# scrapy爬虫框架学习
## 目标网站

- 防爬协议: https://www.douyin.com/robots.txt


## How to use
1. 创建项目
```shell
scrapy startproject douyin
```
2. 创建爬虫
```shell
scrapy genspider douyin douyin.com
```
3. 运行爬虫
```shell
scrapy crawl douyin
```

## 工具

- curl to code : https://curlconverter.com/python/
- https://www.kgtools.cn/convert/curl
- 键值对转换: https://www.toolhelper.cn/Char/KeyValueConvert

## 文档
- scrapy官网: https://scrapy.org/
- 文档: https://docs.scrapy.org/en/latest/index.html
- 中文文档: https://scrapy-16.readthedocs.io/zh-cn/latest/
- 配置国内源: https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

## 问题

### 返回444状态码
https://juejin.cn/post/7184705216095191098

### 无法正确获得页面, 但是返回200状态码



## 方式总结

### 一. 通过抓包工具获取接口数据

### 二. 访问html页面, 通过xpath或者css选择器解析html页面获取数据

### 三. 通过selenium模拟浏览器访问页面, 通过xpath或者css选择器解析html页面获取数据
用 requests 做数据采集面对要登录的网站时，要分析数据包、JS 源码，构造复杂的请求，往往还要应付验证码、JS 混淆、签名参数等反爬手段，门槛较高，开发效率不高。
使用浏览器，可以很大程度上绕过这些坑，但浏览器运行效率不高。

网页自动化工具
- Clicknium: https://clicknium.com/
- selenium: https://www.selenium.dev/documentation/webdriver/getting_started/install_library/   https://github.com/SeleniumHQ/selenium
- DrissionPage: https://github.com/g1879/DrissionPage

## record
分享链接eg
> 3.84 h@B.te daA:/ 08/13  为了预防自然灾害，人类研制出了“天气武器”# 影视推荐 # 燃剪 # 灾难片  https://v.douyin.com/iRdgEGme/ 复制此链接，打开Dou音搜索，直接观看视频！

> 4.87 Ivf:/ C@H.VL 10/24  复制打开抖音，看看【Eva桑的作品】真没拉腿# 05  https://v.douyin.com/iRdt6DAJ/

分享段地址 https://v.douyin.com/iRdt6DAJ/ 302 重定向到真正的视频地址
视频html地址组成: https://www.douyin.com/video/+aweme_id
eg: https://www.douyin.com/video/7271869157971397944


step1: 获取一个接口curl
step2: 修改入参count等, 获取更多数据
step3: 通过三方工具生成X-bogus参数等
step4: 重新组成url, 发起请求, 获取数据
