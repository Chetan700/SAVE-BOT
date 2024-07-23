### 标题
<h1 align="center">
  <b>保存受限内容机器人</b>
</h1> 

联系方式：[Telegram](https://t.me/MaheshChauhan) 

由Mahesh Chauhan制作的稳定Telegram机器人，用于获取自定义缩略图支持的受限消息。

- 适用于公共和私人聊天
- 私人媒体的自定义缩略图支持
- 支持文本和网页媒体消息
- 更快的速度
- 强制订阅功能
- 要从机器人保存，发送此格式的链接：`t.me/b/bot_username/message_id`（使用Plus Messenger获取message_id）
- `/batch` - （仅限所有者）使用此命令一次最多保存来自私人或公共受限频道的100个文件。
- `/cancel` - 使用此命令停止批量处理
- 增加了时间延迟以避免FloodWait并保持用户账户安全。

### 变量

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT_TOKEN` 
- `AUTH` - 所有者用户ID
- `FORCESUB` - 公共频道用户名，不包含'@'。不要忘记将机器人作为管理员添加到频道中。

### 获取API和PYROGRAM字符串会话：

API: [API抓取机器人](https://t.me/USETGSBOT) 或 [Telegram.org](https://my.telegram.org/auth) 

PYROGRAM会话: [SessionGen机器人](https://t.me/SessionStringGeneratorRobot) 或 [![在Repl.it上运行](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@levinalab/Session-Generator#main.py) 

BOT令牌: 电报上的@Botfather

### 部署

在`VPS`上部署

简单方法：

- 安装docker-compose
- 使用您喜欢的文本编辑器或nano填写docker-compose.yml文件中的变量
- 启动容器

```
sudo apt install docker-compose -y
nano docker-compose.yml
sudo docker-compose up --build
```

困难方法：

- 在[这个](https://github.com/vasusen-code/SaveRestrictedContentBot/blob/master/main/__init__.py)文件中填写您的分叉中的变量，如[此图](https://t.me/MaheshChauhan/36)所示
- 输入以下所有命令

```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
```

- 如果您希望机器人在后台运行，则在`python3 -m main`之前输入`screen -S srcb`
- 在`python3 -m main`之后，点击ctrl+A，ctrl+D
- 如果您想要停止机器人，那么输入`screen -r srcb`，要杀死屏幕输入`screen -S srcb -X quit`。

在`Render`上部署您的机器人

教程 - [点击这里](https://telegra.ph/SRCB-on-Render-05-17) 

在`heroku`上部署您的机器人

方法1：
- 星标仓库，并在桌面模式下分叉它
- 转到分叉仓库的设置
- 将您的仓库重命名为其他名称
- 点击[![部署](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

方法2：
- 星标仓库，并在桌面模式下分叉它
- 在heroku上创建应用程序
- 转到应用程序设置> config vars> 添加所有变量
- 添加构建包
- 连接到GitHub并部署
- 打开dynos

手动部署的构建包：

- `heroku/python`
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git` 

在`Okteto`上部署您的机器人[无用]

Okteto教程 - [点击这里](https://telegra.ph/Okteto-Deploy-04-01) 

[![在Okteto上开发](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com) 
