import json
from typing import Optional


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