# vktools
__Инструменты для удобной работы с vk_api__

### Все нужные импорты
![example imports](https://github.com/Fsoky/vktools/blob/main/images/Screenshot_0.png)

### Keyboard

```py
from vktools import Keyboard, ButtonColor, Text, OpenLink, Location # Еще имеются VkApps, VkPay

keyboard = Keyboard(
	[
		[
			Text("RED", ButtonColor.NEGATIVE),
			Text("GREEN", ButtonColor.POSITIVE),
			Text("BLUE", ButtonColor.PRIMARY),
			Text("WHITE")
		],
		[
			OpenLink("YouTube", "https://youtube.com/c/Фсоки"),
			Location()
		]
	]
)

vk.messages.send(user_id=event.user_id, message="Test Keyboard", keyboard=keyboard.add_keyboard())
```
![example keyboard](https://github.com/Fsoky/vktools/blob/main/images/Screenshot_1.png)

![example code of keyboard](https://github.com/Fsoky/vktools/blob/main/images/Screenshot_3.png)

### Карусели (*template*)

```py
from vktools import Keyboard, ButtonColor, Carousel, Element

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

vk.messages.send(user_id=event.user_id, message="Test Keyboard", template=carousel.add_carousel())
```

![example carouseles](https://github.com/Fsoky/vktools/blob/main/images/Screenshot_2.png)

![example code of carouseles](https://github.com/Fsoky/vktools/blob/main/images/Screenshot_4.png)

## Example code

```py
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


from vktools import Keyboard, ButtonColor, Text, OpenLink, Location

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
						Text("RED", ButtonColor.NEGATIVE),
						Text("GREEN", ButtonColor.POSITIVE),
						Text("BLUE", ButtonColor.PRIMARY),
						Text("WHITE")
					],
					[
						OpenLink("YouTube", "https://youtube.com/c/Фсоки"),
						Location()
					]
				]
			)

			send_message(user_id, "VkTools Keyboard by Fsoky ~", keyboard)

		elif text == "test carousel":
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
```