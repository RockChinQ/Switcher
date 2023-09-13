# ContentGenerator Switcher for QChatGPT

### 使用此插件，要求QChatGPT版本等于或高于`v2.3.4`

[QChatGPT](https://github.com/RockChinQ/QChatGPT)项目的内容生成器（模型）切换插件  
使用此插件以方便地在`GPT-3`、`GPT-3.5`、`New Bing`等语言模型间切换

## 已适配

### 文字对话

#### 主线Completion接口

- [x] GPT-3 (`text-davinci-003`)

#### 主线ChatCompletion接口

- [x] GPT-3.5 (`gpt-3.5-turbo`)
- [x] GPT-4 (`gpt-4`)

#### [RevLibs插件](https://github.com/RockChinQ/revLibs)接入

- [x] ChatGPT逆向 (网页版3.5)
- [ ] ChatGPT逆向 (网页版4)
- [x] New Bing逆向
- [x] HuggingChat逆向

#### 通过[One API](https://github.com/songquanpeng/one-api)接入

需要QChatGPT版本高于`v2.5.3`，确保已在One API配置好渠道，并已在`config.py`设置反向代理地址和key。

- [x] 讯飞星火大模型
- [x] 智谱ChatGLM-Pro/Std/Lite
- [x] 阿里通义千问-V1/Plus-V1
- [x] 百度文心千帆ERNIE-Bot/ERNIE-Bot-Turbo

## 安装

使用管理员账号私聊机器人账号发送命令
```
!plugin get https://github.com/RockChinQ/Switcher
```

## 使用

管理员发送指令
```
!switch
```
查看当前支持的模型，并根据指引切换