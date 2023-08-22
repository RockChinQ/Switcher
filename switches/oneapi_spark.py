from .model import AbstractSwitch


class OneAPISpark(AbstractSwitch):
    """OneAPI 星火大模型"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 讯飞星火大模型"

    @staticmethod
    def get_alias() -> str:
        return "spark"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'SparkDesk'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']

