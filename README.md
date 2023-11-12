>
> 免责声明：
>
> 1. **仅供学习与交流：** 本文仅供学习和交流之用途，作者并不对其中的任何信息的准确性、完整性或实用性作出保证。读者在使用这些信息时应自行判断，并对其行为负全部责任。
> 2. **知识更新：** 由于知识不断更新，本文的内容可能已过时或不再准确。读者在应用其中的观点、建议或信息时，请注意核实并参考最新的可靠来源。
> 3. **个人观点：** 本文中的观点和建议仅代表作者个人，不代表任何机构或组织的观点。读者应理性对待这些观点，并在需要时寻求专业意见。
> 4. **风险承担：** 读者在采纳本文中的建议或信息时，应自行承担相应的风险。作者不对任何由此产生的直接或间接损失负责。
> 5. **版权声明：** 本文的知识产权归作者所有。未经授权，禁止任何形式的转载、复制或修改。读者如需使用本文内容，请事先取得作者的书面许可。
> 6. **法律责任：** 本文仅为作者个人的观点和经验总结，不构成法律、金融或专业建议。读者在遇到法律问题时应咨询专业律师，并在做出决策前充分了解相关法规。
>
> 通过阅读本文，您表明已经阅读并同意接受上述免责声明的所有条款。如果您不同意这些条款，请不要使用本文提供的信息。



---



## 使用样例
![img.png](img.png)

![image-20231112151407890](http://qiniu.yujing.icu/typora_img/image-20231112151407890.png)

运行效果

![image-20231112151429637](http://qiniu.yujing.icu/typora_img/image-20231112151429637.png)

运行结果

![image-20231112151517139](http://qiniu.yujing.icu/typora_img/image-20231112151517139.png)



















---

以下大部分是大多数是边学习边做的, 有很多测试/笔记, 记录得比较乱..., 会阅读得很困难不通顺是正常的, 因为就是想到一点记一点


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


## todo

- 完善日志
- 完全视频下载统计
- 使用FFmpeg获取视频信息
- https://jeremylee.sh/bins/
- https://pypi.org/project/python-ffmpeg/
- 图文下载? 图文"images"字段不为null, 一张图4个地址; 视频url变为mp3
- 下载个人喜欢的视频/收藏夹