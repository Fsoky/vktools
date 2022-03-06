# VkTools - дополнительные инструменты для vk-api

### Инструменты 🛠
![Python](https://img.shields.io/badge/Python-3.8-blue?style=for-the-badge&logo=python)
![Json](https://img.shields.io/badge/json-red?style=for-the-badge&logo=json)
![typing](https://img.shields.io/badge/typing-orange?style=for-the-badge)

### Установка 💾
- Установка, используя пакетный менеджер pip
```
$ pip install vktools
```
- Установка с GitHub *(требуется [git](https://git-scm.com/downloads))*
```
$ git clone https://github.com/Fsoky/vktools
$ cd vktools
$ python setup.py install
```
- Или
```
$ pip install git+https://github.com/Fsoky/vktools
```

### Клавиатура
```py
from vktools import Keyboard, ButtonColor, Text, OpenLink, Location

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
```
`.add_keyboard()` - получить JSON клавиатуры
`.get_empty_keyboard()` - Удалить клавиатуру

![Keyboard](https://github.com/Fsoky/vktools/blob/main/images/keyboard_image.png)

### Карусель
```py
from vktools import Keyboard, ButtonColor, Text, Carousel, Element

carousel = Carousel(
    [
        Element(
            "The First Title",
            "The First Description",
            "-000000_1111111", # ID фотографии
            "https://vk.com/fsoky", # Редирект при клике
            [Text("Button 1", ButtonColor.POSITIVE)]
        ),
        Element(
            "The Second Title",
            "The Second Description",
            "-000000_1111111",
            "https://vk.com/fsoky",
            [Text("Button 2", ButtonColor.NEGATIVE)]
        )     
    ]
)
```
`.add_carousel()` - Получить JSON карусели

![Carousel](https://github.com/Fsoky/vktools/blob/main/images/carousel_image.png)

### Присоединяйся к нам
[![Vkontakte](https://img.shields.io/badge/Vkontakte-black?style=for-the-badge&logo=VK)](https://vk.com/fsoky)
[![YouTube](https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=YouTube)](https://youtube.com/c/Фсоки)
[![Telegram](https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=Telegram)](https://t.me/fsokycommunity)
