import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vktools import Keyboard, ButtonColor, Text, Carousel, Element

vk = vk_api.VkApi(token="token")


def send_message(user_id, message, carousel=None):
    values = {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    }

    if carousel is not None:
        values["template"] = carousel.add_carousel()

    vk.method("messages.send", values)


for event in VkLongPoll(vk).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == "test carousel":
            carousel = Carousel(
                [
                    Element(
                        "Title 1",
                        "Description 1",
                        "-203980592_457239030", # photo_id
                        "https://vk.com/fsoky", # redirect url, if user click on element
                        [Text("Button 1", ButtonColor.POSITIVE)]
                    ),
                    Element(
                        "Title 2",
                        "Description 2",
                        "-203980592_457239030", # photo_id
                        "https://vk.com/fsoky", # redirect url, if user click on element
                        [Text("Button 2", ButtonColor.PRIMARY)]
                    )
                ]
            )

            send_message(user_id, "VkTools Carousel by Fsoky ~", carousel=carousel)