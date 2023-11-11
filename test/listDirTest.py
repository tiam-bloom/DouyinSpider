# _*_ coding : UTF-8 _*_
# @Time : 2023/11/12 0:29
# @Auther : Tiam
# @File : listDirTest
# @Project : DouyinSpider
# @Desc :
import os


save_json_dir_path = r'F:\Tiam\Desktop\JustPlay\Python\DouyinSpider\v1\data\MS4wLjABAAAA-WH0IauwbSxT1keTMQXBJzL8K_fenFLLzvMF2lDoJ6Y\json'
for file_name in os.listdir(save_json_dir_path):
    print(os.path.join(save_json_dir_path, file_name))


alist = []
b = [1, 2, 3]
# 合并列表
alist.extend(b)
alist.extend([4, 5, 6])
print(alist)