import json
from typing import Optional


class Tools:

	def __init__(self, vk):
		self.vk = vk

	def get_id(self, screen_name):
		return self.vk.method("utils.resolveScreenName", {"screen_name": screen_name, "v": 5.21})["object_id"]


class Keyboard:

	def __init__(self, button: list, one_time=False, inline=False):
		self.one_time = one_time
		self.inline = inline

		self.keyboard = {
			"one_time": self.one_time,
			"inline": self.inline,
			"buttons": button
		}

	def add_keyboard(self):
		obj = json.dumps(self.keyboard, ensure_ascii=False).encode("utf-8")
		return obj.decode("utf-8")


class ButtonColor:

	NEGATIVE = "negative"
	POSITIVE = "positive"
	PRIMARY = "primary"
	SECONDARY = "secondary"


class Text:

	def __new__(cls, label: Optional[str], color: Optional[str]="secondary", payload: Optional[str]=None):
		return {
			"action": {
				"type": "text",
				"label": label,
				"payload": payload
			},
			"color": color
		}


class OpenLink:

	def __new__(cls, label: Optional[str], link: Optional[str], payload: Optional[str]=None):
		return {
			"action": {
				"type": "open_link",
				"label": label,
				"link": link,
				"payload": payload
			}
		}


class Location:

	def __new__(cls, payload: Optional[str]=None):
		return {
			"action": {
				"type": "location",
				"payload": payload
			}
		}


class VkPay:

	def __new__(cls, pay_hash: Optional[str], payload: Optional[str]=None):
		return {
			"action": {
				"type": "vkpay",
				"hash": pay_hash,
				"payload": payload
			}
		}


class VkApps:

	def __new__(cls, app_id: Optional[int], owner_id: Optional[int], label: Optional[str], app_hash: Optional[str], payload: Optional[str]=None):
		return {
			"action": {
				"type": "vkapps",
				"app_id": app_id,
				"owner_id": owner_id,
				"label": label,
				"hash": app_hash,
				"payload": payload
			}
		}


class Carousel(object):

	def __init__(self, carousel: list):
		self.carousel = carousel

	def add_carousel(self):
		obj = json.dumps(
			{
				"type": "carousel",
				"elements": self.carousel
			},
			ensure_ascii=False
		).encode("utf-8")

		return obj.decode("utf-8")


class Element:

	def __new__(cls, title: Optional[str]=None, description: Optional[str]=None, photo_id: Optional[str]=None, link: Optional[str]=None, buttons: Optional[list]=None, template_type: str="open_link"):
		if template_type == "open_link":
			return {
				"title": title,
				"description": description,
				"action": {
					"type": "open_link",
					"link": link
				},
				"photo_id": photo_id,
				"buttons": buttons
			}
		elif template_type == "open_photo":
			return {
				"title": title,
				"description": description,
				"photo_id": photo_id,
				"action": {
					"type": "open_photo"
				},
				"buttons": buttons
			}
		else:
			raise ValueError("Parametr template_type have: open_link or open_photo")

class CarouselButton(object):

	@staticmethod
	def element(buttons: list, link, title=None, description=None, photo_id=None):
		return {
			"title": title,
			"description": description,
			"action": {
				"type": "open_link",
				"link": link
			},
			"photo_id": photo_id,
			"buttons": buttons
		}

	@staticmethod
	def element_photo(buttons: list, photo_id=None, title=None, description=None):
		return {
			"title": title,
			"description": description,
			"photo_id": photo_id,
			"action": {
				"type": "open_photo"
			},
			"buttons": buttons
		}

	def openlink(self, elems: list):
		values = {
			"type": "carousel"
		}
		values["elements"] = elems

		return values

	def openphoto(self, elems: list):
		values = {
			"type": "carousel"
		}
		values["elements"] = elems

		return values