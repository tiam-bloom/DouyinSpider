# _*_ coding : UTF-8 _*_
# @Time : 2023/11/6 11:29
# @Auther : Tiam
# @File : main1
# @Project : DouyinSpider
import json

with open('../params/鞠婧祎-count-64.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    aweme_list = json_data['aweme_list']
    print(len(aweme_list))  # 41
