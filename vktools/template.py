import json
from typing import Any

from .keyboard import Text, OpenLink, Location, VkPay, VkApps, OpenApp, Callback


class Element:

    def __new__(
        cls,
        title: str | None=None,
        description: str | None=None,
        photo_id: str | None=None,
        link: str | None=None,
        buttons: list[
            Text | OpenLink | Location | VkPay | VkApps | OpenApp | Callback
        ] | None=None,
        template_type: str="open_link"
    ) -> dict[str, Any] | None:
        element = {
            "title": title,
            "description": description,
            "photo_id": photo_id,
            "buttons": buttons
        }
        
        if template_type == "open_link":
            element["action"] = {
                "type": "open_link",
                "link": link
            }
        elif template_type == "open_photo":
            element["action"] = {
                "type": "open_photo"
            }
        else:
            raise ValueError("Parameter template_type have: open_link or open_photo")
        return element
        

class Carousel:

    def __init__(self, elements: list[Element]) -> None:
        self.elements = elements

    def add_carousel(self) -> str:
        obj = json.dumps(
            {
                "type": "carousel",
                "elements": self.elements
            },
            ensure_ascii=False
        ).encode("utf-8")
        return obj.decode("utf-8")