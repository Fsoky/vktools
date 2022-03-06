import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vktools import Keyboard, ButtonColor, Text

vk = vk_api.VkApi(token="")
api = vk.get_api()


def send_message(user_id, message, **kwargs):
    api.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        **kwargs
    )


for event in VkLongPoll(vk).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        keyboard = Keyboard(
            [
                [
                    Text("Test Button", ButtonColor.POSITIVE)
                ]
            ]
        )

        if event.text == "keyboard":
            send_message(event.user_id, "Look at this keyboard", keyboard=keyboard.add_keyboard())
        elif event.text == "delete":
            send_message(event.user_id, "Where is my keyboard?", keyboard=keyboard.get_empty_keyboard())
