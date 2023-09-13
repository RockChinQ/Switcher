from .model import AbstractSwitch


class OneAPIERNIE(AbstractSwitch):
    """OneAPI 百度文心千帆"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 百度文心千帆ERNIE-Bot"

    @staticmethod
    def get_alias() -> str:
        return "ERNIE-bot"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'ERNIE-Bot'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


class OneAPIERNIETurbo(AbstractSwitch):
    """OneAPI 百度文心千帆"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 百度文心千帆ERNIE-Bot-Turbo"

    @staticmethod
    def get_alias() -> str:
        return "ERNIE-bot-turbo"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'ERNIE-Bot-turbo'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']



