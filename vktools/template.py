import json
from typing import List, Dict, Any, Union, Optional

from .keyboard import Text, OpenLink, Location, VkPay, VkApps


class Element:

    def __new__(
        cls,
        title: Optional[str] | None=None,
        description: Optional[str] | None=None,
        photo_id: Optional[str] | None=None,
        link: Optional[str] | None=None,
        buttons: Optional[
            List[
                Union[
                    Text,
                    OpenLink,
                    Location,
                    VkPay,
                    VkApps
                ]
            ]
        ] | None=None,
        template_type: str="open_link"
    ) -> Union[Optional[Dict[str, Any]], None]:
        element: Dict[str, Any] = {
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

    def __init__(self, elements: List[Element]) -> None:
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