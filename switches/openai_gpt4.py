from .model import AbstractSwitch

class OpenAIGPT4(AbstractSwitch):
    """OpenAI GPT4"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OpenAI GPT-4.0官方API"

    @staticmethod
    def get_alias() -> str:
        return "gpt4"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'gpt-4'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


class OpenAIGPT4_32K(AbstractSwitch):
    """OpenAI GPT4-32K"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OpenAI GPT-4.0-32k官方API"

    @staticmethod
    def get_alias() -> str:
        return "gpt4-32k"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'gpt-4-32k'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


