> 这里以鞠婧祎的个人主页为demo
>
> https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz
>
> 【2023-11-4 23:02:52 星期六】可能后面随着抖音的调整, 方法不再适用, 请注意





## 找到接口

找到`https://www.douyin.com/aweme/v1/web/aweme/post/`路劲的接口

![image-20231104230515850](http://qiniu.yujing.icu/typora_img/image-20231104230515850.png)

预览响应数据, 应该是能跟所发布视频的描述所对应的就OK, 但是只只有18条数据

余下的数据, 滚动进度条的时候就会出来了

> 接口整整37个参数, 随便改一个都会导致请求不到数据(返回状态码200, 但就是没数据), 没想到解决办法....

![image-20231104230815754](http://qiniu.yujing.icu/typora_img/image-20231104230815754.png)

将返回的数据保存到json文件中

![image-20231104231435708](http://qiniu.yujing.icu/typora_img/image-20231104231435708.png)

## 下载视频



```py
import requests
import json
import os

# todo 错误处理
def download_video(url, path):
    print('\n开始下载视频...', path.split('/')[-1])
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        # 进度条
        total_length = int(r.headers.get('content-length'))
        print('视频大小:', total_length)
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
            # 打印进度条
            print('\r' + '[下载进度]:%s%.2f%%' % (
                '>' * int((f.tell() / total_length) * 50), float(f.tell() / total_length) * 100), end='')


index = 0

# json_file, 接口返回的json文件位置
# save_file_dir, 保存视频的文件夹路径
def save_video_batch(json_file, save_file_dir):
    global index
    if not os.path.exists(save_file_dir):
        os.makedirs(save_file_dir)
    # 读取json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        aweme_list = json_data['aweme_list']
        for aweme in aweme_list:
            video_url_list = aweme['video']['play_addr']['url_list']
            video_name = aweme['desc']
            # 一个视频有三个地址, 成功一个就break
            index += 1
            for video_url in video_url_list:
                # print(video_url)
                try:
                    download_video(video_url, f'{save_file_dir}{index}-{video_name}.mp4')
                    break
                except Exception as e:
                    print('下载失败')


save_video_batch('../params/鞠婧祎主页.json', '../data/鞠婧祎主页/')
```

## 下载结果

![image-20231104232212786](http://qiniu.yujing.icu/typora_img/image-20231104232212786.png)



> 抖音反爬感觉做的很好, 好难爬....
>
> 尝试直接去获取html页面, 解析html页面, 但是获取的html页面并不是实际浏览器中浏览的页面(不是验证码界面我看了)
>
> 
>
> 请求接口也是, API调试工具中能请求到, 但是使用代码就不行了, 也是返回200状态, 但是没有数据, 下面是代码, 不知道缺了什么
>
> (有些我觉得敏感的数据, 需要自己替换)

`````py
import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'cookie',   # 替换自己的cookie
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
}

params = (
    ('device_platform', 'webapp'),
    ('aid', '6383'),
    ('channel', 'channel_pc_web'),
    ('sec_user_id', 'MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs'),
    ('max_cursor', '1696500302000'),
    ('locate_query', 'false'),
    ('show_live_replay_strategy', '1'),
    ('need_time_list', '0'),
    ('time_list_query', '0'),
    ('whale_cut_token', ''),
    ('cut_version', '1'),
    ('count', '18'),
    ('publish_video_strategy_type', '2'),
    ('pc_client_type', '1'),
    ('version_code', '170400'),
    ('version_name', '17.4.0'),
    ('cookie_enabled', 'true'),
    ('screen_width', '1707'),
    ('screen_height', '1067'),
    ('browser_language', 'zh-CN'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Edge'),
    ('browser_version', '118.0.2088.76'),
    ('browser_online', 'true'),
    ('engine_name', 'Blink'),
    ('engine_version', '118.0.0.0'),
    ('os_name', 'Windows'),
    ('os_version', '10'),
    ('cpu_core_num', '16'),
    ('device_memory', '8'),
    ('platform', 'PC'),
    ('downlink', '10'),
    ('effective_type', '4g'),
    ('round_trip_time', '50'),
    ('webid', '7297499797400897065'),
    ('msToken', 'xxx'),  # 替换token
    ('X-Bogus', 'xxx'),  # 替换
)

response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', headers=headers, params=params)
# 响应200, 
print(response.status_code)
# 但是没有数据
print(response.text)
`````



> 现在的方法还很麻烦, 有待改进, 
>
> 设想我只需要输入主页的url地址, 比如`https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz`, 自动下载主页中所有视频





## 对比分页url不同处

![image-20231105013709278](http://qiniu.yujing.icu/typora_img/image-20231105013709278.png)

第一页

max_cursor=0

need_time_list=1     # 为1时返回`time_list`字段

`msToken=LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI=&X-Bogus=DFSzswVYqXkANCMrtFQrGBt/pLfc`



第三页

max_cursor=1663149600000  

need_time_list=0    # 为0时`time_list`字段为`null`

`msToken=A41sEsiFWmGEjiWR5Iw-FMW56zgRYH4n6Lme1yc_t8GktnxZbPKzr3VfTxFu0r50JjGEw2gQBK5laYu1uzwij6OO6-M600sLF1Th9_-LjFmdZGr7tujnJb3Pm9A_ZcA=&X-Bogus=DFSzswVu6JGANx/ItFQrPat/pLfE`



`header中cookie不同`





> 关键词: `msToken`、`X-Bogus`、`webmssdk.js`、`JSVMP`、`WebAssembly` 

msToken参考

- https://github.com/5ime/Tiktok_Signature
- [【WEB逆向】关于tiktok参数msToken，X-Bogus，_signature生成_H(小何)的博客-CSDN博客](https://blog.csdn.net/weixin_46874932/article/details/130829694)
- https://www.52pojie.cn/thread-1631492-1-1.html
- https://sf16-secsdk.ttwstatic.com/obj/rc-web-sdk-gcs/webmssdk/1.0.0.195/webmssdk.js



js混淆/反爬之jsvmp

- https://jsvmp.com/CN/index.html
- https://blog.jsvmp.com/
- https://cdmd.cnki.com.cn/Article/CDMD-10697-1018118675.htm





> WebAssembly或称wasm是一个低级编程语言。WebAssembly是便携式的抽象语法树，被设计来提供比JavaScript更快速的编译及执行。WebAssembly将让开发者能运用自己熟悉的编程语言编译，再藉虚拟机引擎在浏览器内执行。 [维基百科](https://zh.wikipedia.org/zh-cn/WebAssembly)

JSVMP 的逆向方法: RPC 远程调用，补环境，日志断点还原算法







以下摘自: [B1gM8c/X-Bogus: 抖音X-Bogus生成接口 (github.com)](https://github.com/B1gM8c/X-Bogus)

### [msToken生成](https://github.com/B1gM8c/X-Bogus#mstoken生成)

这里Cookie指的一提的是`msToken`可以是随机107位大小写英文字母、数字生成，以下是一个简单的样例

```
    def generate_random_str(self, randomlength=107):
        """
        根据传入长度产生随机字符串
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
        length = len(base_str) - 1
        for _ in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        return random_str
```



### [ttwid生成](https://github.com/B1gM8c/X-Bogus#ttwid生成)

当然，部分网友也分析了`ttwid`的生成方式，你可以通过POST请求`https://ttwid.bytedance.com/ttwid/union/register/`，请求体使用JSON格式

```
{"region":"cn","aid":1768,"needFid":false,"service":"www.ixigua.com","migrate_info":{"ticket":"","source":"node"},"cbUrlProtocol":"https","union":true}
```



然后在响应头的`Set-Cookie`中，你可以获得`ttwid`

```
ttwid=1%7C7ZLJzwjjEw7NLeADTpVd-3eId-ZEIg0jpCEzTV9p_2A%7C1677681848%7C4ff4f97328ddc18b6d46c259bc26a05d2e654b50e3f21b27b8f9e9e8f9fcec82; Path=/; Domain=bytedance.com; Max-Age=31536000; HttpOnly; Secure
```



只需要稍加提取就可以使用了

```
ttwid=1%7C7ZLJzwjjEw7NLeADTpVd-3eId-ZEIg0jpCEzTV9p_2A%7C1677681848%7C4ff4f97328ddc18b6d46c259bc26a05d2e654b50e3f21b27b8f9e9e8f9fcec82;
```





http://xyz34.fan/

header 中三个关键的参数`cookie`、`referer`、`user-agent`

cookie中最重要的就是`ttwid`  （现在`ttwid`作为了游客ID，权重甚至超过了校验参数 s_v_web_id， 摘自：http://www.lxspider.com/?p=299）





x-bogus: 28位的x_bogus, X-Bogus会对params、form-data、user-agent、时间、canvas进行校验。

## 测试





## 分页

第一页

```bash
curl 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7297962636765939237&msToken=l-BJ6bqIdyeXxkOdAwRoFCLDuMFkPB_TdQbQ1OoHBDjHo_Zu0OC-NHFCZERAZahw3v63RUklqslgEHeBPXnT_7jKviOvs5NQKPLNbJqvYvapVwpcPJzGAHircBpQ6PWSig==&X-Bogus=DFSzswVYYVJANcR2tFnbUFBQJW0V' \
  -H 'authority: www.douyin.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'cookie: cookie' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz' \
  -H 'sec-ch-ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0' \
  --compressed
```



max_cursor=0

need_time_list=1

msToken/X-Bogus 不同



其中返回值max_cursor=1690955655000, 作为下一页的参数



第二页

```bash
curl 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=1690955655000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7297962636765939237&msToken=F76Dl6jVHMRzcyNVmUyQz5dlD947k3ZR7HV_TO3FF6WtVsJpdVliWE8Ivohl6dt1xoSmUznHvv0yHW8f57mZS7JkwKuOd0YNQeqkukBsQpyEKUyA0SSEbKsucneqjiEuYA==&X-Bogus=DFSzswVYCRTANcR2tFnbUlBQJW8q' \
  -H 'authority: www.douyin.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'cookie: cookie' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz' \
  -H 'sec-ch-ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0' \
  --compressed
```



max_cursor=1690955655000   2023-08-02 05:54:15

need_time_list=0





第三页

```bash
curl 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=1666665000000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7297962636765939237&msToken=0XR4cwC8FQ4R2HEpJTgy5Ks9tLxtuTQy94HSA7LF_00iHuy-SoHN4YzJA-ddQEaxtDnNxeGjOLhTVUoNdfxlXd6EMBNqPHZN7Lz8TnMHum0_MeAKSshDBbbzsgnlrsHZJQ==&X-Bogus=DFSzswVYiebANcR2tFnbUMBQJW8P' \
  -H 'authority: www.douyin.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'cookie: cookie' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz' \
  -H 'sec-ch-ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0' \
  --compressed
```

max_cursor=1666665000000    2022-10-25 02:30:00





最后页

```bash
curl 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=1611220344000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7297962636765939237&msToken=0XR4cwC8FQ4R2HEpJTgy5Ks9tLxtuTQy94HSA7LF_00iHuy-SoHN4YzJA-ddQEaxtDnNxeGjOLhTVUoNdfxlXd6EMBNqPHZN7Lz8TnMHum0_MeAKSshDBbbzsgnlrsHZJQ==&X-Bogus=DFSzswVYTFvANcR2tFnoAMBQJW8K' \
  -H 'authority: www.douyin.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'cookie: cookie' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz' \
  -H 'sec-ch-ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0' \
  --compressed
```

has_more = 0





不同用户sec_user_id参数不同

header中的referer不同





先生成msToken

再携带参数, 包括msToken(不包括X-bogus), 获取X-bogus和ttwid

发送请求
