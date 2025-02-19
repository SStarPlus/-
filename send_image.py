import os
import json
import requests

# 读取当前序号
with open('current_index.txt', 'r') as f:
    current_index = int(f.read().strip())

# 读取图片列表
with open('images.json', 'r') as f:
    images = json.load(f)

# 获取当前图片 URL
image_url = images[current_index % len(images)]

# 发送消息到钉钉机器人
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=88b323167a8414e923c5765901aadca94d40004e348b80bee561e2262a1c2f8e"
headers = {"Content-Type": "application/json"}
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "每日图片",
        "text": f"![图片]({image_url})"
    }
}
response = requests.post(webhook_url, json=data, headers=headers)

# 更新序号
new_index = current_index + 1
with open('current_index.txt', 'w') as f:
    f.write(str(new_index))

# 提交更改到 GitHub（需配置 Git 自动提交）
os.system('git config --global user.name "GitHub Actions"')
os.system('git config --global user.email "actions@github.com"')
os.system('git add current_index.txt')
os.system('git commit -m "Update current index"')
os.system('git push')