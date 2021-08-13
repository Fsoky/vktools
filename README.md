# vktools
Tools for vk_api for comfort work

![example imports](https://github.com/Fsoky/vktools/images/blob/main/Screenshot_0.png)

![example keyboard](https://github.com/Fsoky/vktools/images/blob/main/Screenshot_1.png)

![example code of keyboard](https://github.com/Fsoky/vktools/images/blob/main/Screenshot_2.png)

![example carousel](https://github.com/Fsoky/vktools/images/blob/main/Screenshot_3.png)

![example code of carousel](https://github.com/Fsoky/vktools/images/blob/main/Screenshot_4.png)

## Example code
```py
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


from vktools import Keyboard, KeyboardButton, Carousel, CarouselButton

vk = vk_api.VkApi(token="token")


def send_message(user_id, message, keyboard=None, carousel=None):
	values = {
		"user_id": user_id,
		"message": message,
		"random_id": 0
	}

	if keyboard is not None:
		values["keyboard"] = keyboard.add_keyboard()
	if carousel is not None:
		values["template"] = carousel.add_carousel()

	vk.method("messages.send", values)

for event in VkLongPoll(vk).listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text.lower()
		user_id = event.user_id

		if text == "test":
			keyboard = Keyboard(
				[
					[
						KeyboardButton().text("RED", "negative"),
						KeyboardButton().text("GREEN", "positive"),
						KeyboardButton().text("BLUE", "primary"),
						KeyboardButton().text("WHITE")
					],
					[
						KeyboardButton().openlink("YouTube", "https://youtube.com/c/Фсоки")
					],
					[
						KeyboardButton().location()
					]
				]
			)

			send_message(user_id, "VkTools Keyboard by Fsoky ~", keyboard)
		elif text == "test carousel":
			carousel = Carousel(
				[
					CarouselButton().openlink(
						[
							CarouselButton().element(
								title="Title 1",
								description="Description 1",
								photo_id="-203980592_457239030",
								link="https://vk.com/fsoky",
								buttons=[KeyboardButton().text("Button 1", "positive")]
							),
							CarouselButton().element(
								title="Title 2",
								description="Description 2",
								photo_id="-203980592_457239029",
								link="https://vk.com/fsoky",
								buttons=[KeyboardButton().text("Button 2", "negative")]
							)
						]
					)
				]
			)

			send_message(user_id, "VkTools Carousel by Fsoky ~", carousel=carousel)
```