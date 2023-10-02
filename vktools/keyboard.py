import json
from enum import Enum
from typing import List, Dict, Any, Union, Optional


class ButtonColor(Enum):
    NEGATIVE: str = "negative"
    POSITIVE: str = "positive"
    PRIMARY: str = "primary"
    SECONDARY: str = "secondary"


class Text:

    def __new__(
        cls,
        label: str,
        color: ButtonColor=ButtonColor.SECONDARY,
        payload: Optional[str] | None=None
    ) -> Dict[str, Union[str, Dict[str, str], None]]:
        return {
            "action": {
                "type": "text",
                "label": label,
                "payload": payload
            },
            "color": color
        }


class OpenLink:

    def __new__(
        cls,
        label: Optional[str],
        link: Optional[str],
        payload: Optional[str] | None=None
    ) -> Dict[str, Union[str, Dict[str, str], None]]:
        return {
            "action": {
                "type": "open_link",
                "label": label,
                "link": link,
                "payload": payload
            }
        }


class Location:

    def __new__(
        cls,
        payload: Optional[str] | None=None
    ) -> Dict[str, Union[str, Dict[str, str], None]]:
        return {
            "action": {
                "type": "location",
                "payload": payload
            }
        }


class VkPay:

    def __new__(
        cls,
        pay_hash: str,
        payload: Optional[str] | None=None
    ) -> Dict[str, Union[str, Dict[str, str], None]]:
        return {
            "action": {
                "type": "vkpay",
                "hash": pay_hash,
                "payload": payload
            }
        }


class VkApps:

    def __new__(
        cls,
        app_id: int,
        owner_id: int,
        label: str,
        app_hash: str,
        payload: Optional[str] | None=None
    ) -> Dict[str, Union[str, Dict[str, Any], None]]:
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
    

class Keyboard:

    def __init__(
        self,
        button: List[
            Union[
                Text,
                OpenLink,
                Location,
                VkPay,
                VkApps
            ]
        ],
        *,
        one_time: bool=False,
        inline: bool=False
    ) -> None:
        self.one_time = one_time
        self.inline = inline

        self.keyboard: Dict[str, Union[bool, List[Union[Text, OpenLink, Location, VkPay, VkApps]]]] = {
            "one_time": self.one_time,
            "inline": self.inline,
            "buttons": button
        }

    def add_keyboard(self) -> str:
        obj = json.dumps(self.keyboard, ensure_ascii=False).encode("utf-8")
        return obj.decode("utf-8")

    def get_empty_keyboard(self) -> str:
        self.keyboard["buttons"] = []
        return self.add_keyboard()