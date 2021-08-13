import json


class VkTools:

	def __init__(self, vk):
		self.vk = vk

	def get_id(self, screen_name):
		return self.vk.method("utils.resolveScreenName", {"screen_name": screen_name, "v": 5.21})["object_id"]


class Keyboard(object):

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


class KeyboardButton(object):

	def text(self, label, color="secondary", payload=None):
		return {
			"action": {
				"type": "text",
				"label": label,
				"payload": payload
			},
			"color": color
		}

	def openlink(self, label, link, payload=None):
		return {
			"action": {
				"type": "open_link",
				"label": label,
				"link": link,
				"payload": payload
			}
		}

	def location(self, payload=None):
		return {
			"action": {
				"type": "location",
				"payload": payload
			}
		}

	def vkpay(self, pay_hash, payload=None):
		return {
			"action": {
				"type": "vkpay",
				"hash": pay_hash,
				"payload": payload
			}
		}

	def vkapps(self, app_id, owner_id, label, app_hash, payload=None):
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
		obj = json.dumps(self.carousel[0], ensure_ascii=False).encode("utf-8")
		return obj.decode("utf-8")


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