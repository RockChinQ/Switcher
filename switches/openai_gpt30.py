from .model import AbstractSwitch


class OpenAIGPT30(AbstractSwitch):
    """OpenAI GPT3.0"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        pass

    @staticmethod
    def get_alias() -> str:
        pass

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'text-davinci-003'

    @staticmethod
    def disable():
        pass
