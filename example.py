import time

from loguru import logger

from rocketchat_bot_app_bridge.RCBot import RCBot
from rocketchat_bot_app_bridge.definitions.application import IButton
from rocketchat_bot_app_bridge.definitions.message import IMessage
from rocketchat_bot_app_bridge.definitions.user import IUser

bot = RCBot(account_username='testbot')

# it is also possible to set values not through environment
# variables, but by passing them when creating a bot instance
# bot = RCBot(account_username='testbot', # The username must be specified if you
#                                           have entered another account in the application settings
#             port=1444,
#             app_endpoint='http://rocket.chat/api/apps/private/2c3927404e41/sab7/webhook')


# This will be called for every message, unless
# there is a more exact match, for example, hear()
@bot.on_new_message
def new_message(message: IMessage = None):
    logger.info(message['text'])
    msg = IMessage(
        text=f'Нажми на кнопку',
        room=message['room']
    )
    buttons = [
        IButton(text="First button", action='btn1-action', style='primary'),
        IButton(text="DANGER", action='btn-danger-action', style='danger'),
    ]
    bot.send(message=msg, buttons=buttons)


@bot.on_button_click(action='btn1-action')
def click_button(action, user: IUser = None, source_message: IMessage = None):
    msg = IMessage(
        room=source_message['room'],
        text=f'@{user["username"]} clicked on {action}'
    )
    bot.send(message=msg)


# if you use startswith then this function will
# be called on any button whose action starts with this
@bot.on_button_click(startswith='btn-danger-')
def click_button(action, user: IUser = None, source_message: IMessage = None):
    msg = IMessage(
        room=source_message['room'],
        text=f'@{user["username"]} clicked on {action} of button group'
    )
    bot.send(message=msg)


# You can use a regular expression with named groups as in the example.
# Their entry will be passed in the function arguments
@bot.hear(pattern=r"Why (?P<phrase>.*)\??")
def answer_the_question(message: IMessage, phrase):
    msg = IMessage(
        room=message['room'],
        text=f'I don\'t khow why {phrase}...'
    )
    buttons = [
        IButton(text="Mehh );", action='btn-danger-meh', style='danger'),
    ]
    bot.send(message=msg, buttons=buttons)


# The first .run() call will start
# the server to listen for requests
bot.run()

# And here you need an eternal loop for the server to work.
# I wondered if this could be somehow removed.
# Therefore, this is the one todo: find elegant way to hide loop
while True:
    # print("Still alive...")
    time.sleep(300)
