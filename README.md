### This is a RocketChat bot library using an app bridge to create bots with interactive elements such as buttons.
![preview](https://i.imgur.com/zebkL5c.png)
# ☝ Important 
In addition to this description, be sure to see an [example](./example.py) of a bot on how to send and build data to send
# Usage
- First, you **need to install [this application](https://github.com/JargeZ/RocketChat.Apps.BotBridge)** on your rocket chat server.
- Then go to the admin settings -> applications -> BotBridge -> and copy the `POST webhook` address
- In the `Controlled bots` settings field, enter the nickname of the bot user you want to use. Or leave it blank if you want to use the standard `@bbot.bot` account automatically created for the application
- install package with `pip install rocketchat-bot-simple-app-bot` and import this in your project 
  ```
  from rocketchat_bot_app_bridge.RCBot import RCBot
  from rocketchat_bot_app_bridge.definitions.application import IButton
  from rocketchat_bot_app_bridge.definitions.message import IMessage
  from rocketchat_bot_app_bridge.definitions.user import IUser
  ```
- Now you can create a bot instance.\
  `bot = RCBot()`
  If you want to use a custom bot account, then after adding it in the application settings, pass its username like this\
  `bot = RCBot(account_username='testbot')`
- Since communication is carried out in both directions between the RocketChat application and this bot server. Here a web server will be configured on the default port `3228`\
  You can specify your port in the environment variable\
  `export BOT_PORT=12345`
  Also you can pass the port when creating the bot `RCBot (port=12345)` [[[подробнее в файле примаера добавитьссылку]]]
- Also, the link you copied to the `POST webhook` must be passed to the `APP_ENDPOINT` environment variable
  ```
  export APP_ENDPOINT=http://rocket.chat/api/apps/private/2c3927404e41/sab7/webhook
  ```
  Or when created in the same way as the port. more details here.
- Now there are several decorators available to you that you can use on your functions. 
  ```python
  @bot.on_new_message
  def new_message(message: IMessage = None):
      pass
  
  @bot.on_button_click(action='btn1-action')
  def click_button(action, user: IUser = None, source_message: IMessage = None):
      pass
  
  @bot.on_button_click(startswith='btn-danger-')
  def click_button(action, user: IUser = None, source_message: IMessage = None):
      pass
  
  @bot.hear(pattern=r"Why (?P<phrase>.*)\??")
  def answer_the_question(message: IMessage, phrase):
      pass
  ```
- Finally, you need to start the server and wait loop.
  ```python
  bot.run()

  while True:
      time.sleep(300)
  ```
  P.S. Eliminate the need for loop in my todo for easier work
- After launching, there will be a line in the log saying that the server is running.
  ```
  | INFO     | run:57 - Listen on **http://0.0.0.0:3228/** copy this(or service ip for kubernetes) to RocketChat app settings
  ```
You need to specify the address of the server on which the bot is running in the rocket chat settings as a backend address.\
  **Instead of 0.0.0.0, there should be one of your server addresses, which will be available for rocket chat. Eg. Service name in docker-compose or kubernetes**\
  ![](https://i.imgur.com/BI44RUy.png)