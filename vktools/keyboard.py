import json
from typing import Optional


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