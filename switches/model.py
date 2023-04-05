
class AbstractSwitch:
    """开关基类"""

    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def get_name() -> str:
        """获取此开关的名称"""
        raise NotImplementedError

    @staticmethod
    def get_alias() -> str:
        """获取此开关的别名"""
        raise NotImplementedError

    @staticmethod
    def supported() -> bool:
        """获取是否支持使用此开关"""
        raise NotImplementedError

    @staticmethod
    def enable():
        """启用此开关"""
        raise NotImplementedError


__switches__: dict[str, type[AbstractSwitch]] = {}
"""所有开关的字典"""


def register(switch: type[AbstractSwitch]):
    """注册开关"""
    __switches__[switch.get_alias()] = switch


def register_all():
    __switches__ = {}

    from .openai_gpt3 import OpenAIGPT3
    register(OpenAIGPT3)

    from .openai_gpt35 import OpenAIGPT35
    register(OpenAIGPT35)

    from .openai_gpt4 import OpenAIGPT4
    register(OpenAIGPT4)

    from .revchatgpt_gpt35 import RevChatGPT35
    register(RevChatGPT35)

    from .newbing import NewBing
    register(NewBing)

