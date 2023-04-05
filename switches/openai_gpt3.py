from .model import AbstractSwitch


class OpenAIGPT3(AbstractSwitch):
    """OpenAI GPT3.0"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OpenAI GPT-3.0官方API"

    @staticmethod
    def get_alias() -> str:
        return "gpt3"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'text-davinci-003'
