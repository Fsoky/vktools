import json
from enum import Enum
from typing import Any


class ButtonColor(Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return self.value


class Text:

    def __new__(
        cls,
        label: str,
        color: str | ButtonColor=ButtonColor.SECONDARY,
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Text button

        :param label: Button Text. Will be sent by the user to the community dialog
        or conversation when clicked. Maximum length is 40 characters.
        :param color: Button color. The parameter is used only for text and callback buttons.
        Possible values are given below, in the Key Colors section.
        :param payload: Additional information (JSON). In buttons that do not send text,
        it is passed for compatibility with older clients. The maximum is 255 characters.

        - Usage:

        .. code-block:: python
            Text(
                label="My Button",
                color=ButtonColor.PRIMARY, # or "primary"
            )
        """

        return {
            "action": {
                "type": "text",
                "label": label,
                "payload": payload
            },
            "color": color.value if isinstance(color, ButtonColor) else color
        }


class OpenLink:

    def __new__(
        cls,
        label: str | None,
        link: str | None,
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Open link button

        :param label: Button Text.
        :param link: The link to be opened by clicking on the button.
        :param payload: Additional information (JSON). In buttons that do not send text,
        it is passed for compatibility with older clients. The maximum is 255 characters.

        - Usage:

        .. code-block:: python
            OpenLink(
                label="My Button",
                link="https://t.me/fsoky_community"
            )
        """

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
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Location button

        :param payload: Additional information (JSON). It will be returned in the message_new event
        in the field of the same name. Maximum - 255 characters.
        """

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
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Vk Pay button

        :param pay_hash: A string containing VK Pay payment parameters and application ID in aid parameter ,
        separated by &. Example: `action=transfer-to-group&group_id=1&aid=10`.
        The string must not contain the # symbol itself.
        :param payload: Additional information (JSON). It will be returned in the message_new event
        in the field of the same name. Maximum - 255 characters.
        """

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
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Vk Apps button

        :param app_id: The identifier of the called application with the type VK Mini Apps.
        :param owner_id: Identifier of the community in which the application is installed,
        if required to open in a community context.
        :param label: The name of the application indicated on the button.
        :param app_hash: The hash for navigation in the application,
        will be passed in the startup parameter string after the # character.
        Do not add the # character itself to the hash.
        :param payload: Additional information (JSON). It will be returned in the message_new event
        in the field of the same name. Maximum - 255 characters.
        """

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


class OpenApp:

    def __new__(
        cls,
        app_id: int,
        owner_id: int,
        label: str,
        app_hash: str,
        payload: str | None=None,
    ) -> dict[str, Any] | None:
        """
        Open app button

        :param app_id: The identifier of the called application with the type VK Mini Apps.
        :param owner_id: Identifier of the community in which the application is installed,
        if required to open in a community context.
        :param label: The name of the application indicated on the button.
        :param app_hash: The hash for navigation in the application,
        will be passed in the startup parameter string after the # character.
        Do not add the # character itself to the hash.
        :param payload: Additional information (JSON). In buttons that do not send text,
        it is passed for compatibility with older clients. The maximum is 255 characters.
        """

        return {
            "action": {
                "type": "open_app",
                "app_id": app_id,
                "owner_id": owner_id,
                "label": label,
                "hash": app_hash,
                "payload": payload
            }
        }


class Callback:

    def __new__(
        cls,
        label: str,
        payload: str | None=None
    ) -> dict[str, Any] | None:
        """
        Callback button

        :param label: Button text. The maximum length is 40 characters.
        :param payload: Additional information (JSON) returned in the `message_event` event
        in the field of the same name. Maximum - 255 characters.
        """

        return {
            "action": {
                "type": "callback",
                "label": label,
                "payload": payload
            }
        }


class Keyboard:

    def __init__(
        self,
        buttons: list[
            Text | OpenLink | Location | VkPay | VkApps | OpenApp | Callback
        ],
        *,
        one_time: bool=False,
        inline: bool=False
    ) -> None:
        """
        Keyboard

        :param buttons: List of buttons
        :param one_time: Whether to hide the keyboard after pressing a key that sends a message.
        For example: `text` or `location`. Only works for `"inline": false`.
        :param inline: `true` - the keyboard is displayed inside the message. 
        `false` - displays the keyboard in the dialog box, under the message input field.
        """

        self.one_time = one_time
        self.inline = inline

        self.keyboard = {
            "one_time": self.one_time,
            "inline": self.inline,
            "buttons": buttons
        }

    def add_keyboard(self) -> str:
        obj = json.dumps(self.keyboard, ensure_ascii=False).encode("utf-8")
        return obj.decode("utf-8")

    def get_empty_keyboard(self) -> str:
        self.keyboard["buttons"] = []
        return self.add_keyboard()