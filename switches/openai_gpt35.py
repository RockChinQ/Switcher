from .model import AbstractSwitch


class OpenAIGPT35(AbstractSwitch):
    """OpenAI GPT3.5"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OpenAI GPT-3.5官方API"

    @staticmethod
    def get_alias() -> str:
        return "gpt3.5"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'gpt-3.5-turbo'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']

