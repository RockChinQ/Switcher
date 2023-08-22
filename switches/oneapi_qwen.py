from .model import AbstractSwitch


class OneAPIQWEN(AbstractSwitch):
    """OneAPI 阿里通义千问"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 阿里通义千问-V1"

    @staticmethod
    def get_alias() -> str:
        return "qwen-v1"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'qwen-v1'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


class OneAPIQWENPlus(AbstractSwitch):
    """OneAPI 阿里通义千问"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 阿里通义千问-Plus-V1"

    @staticmethod
    def get_alias() -> str:
        return "qwen-plus-v1"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'qwen-plus-v1'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']



