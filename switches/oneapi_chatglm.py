from .model import AbstractSwitch


class OneAPIChatGLMPro(AbstractSwitch):
    """OneAPI 智谱ChatGLM"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 智谱ChatGLM-Pro"

    @staticmethod
    def get_alias() -> str:
        return "chatglm_pro"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'chatglm_pro'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


class OneAPIChatGLMStd(AbstractSwitch):
    """OneAPI 智谱ChatGLM"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 智谱ChatGLM-Std"

    @staticmethod
    def get_alias() -> str:
        return "chatglm_std"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'chatglm_std'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']


class OneAPIChatGLMLite(AbstractSwitch):
    """OneAPI 智谱ChatGLM"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "OneAPI 智谱ChatGLM-Lite"

    @staticmethod
    def get_alias() -> str:
        return "chatglm_lite"

    @staticmethod
    def supported() -> bool:
        return True

    @staticmethod
    def enable():
        import config
        config.completion_api_params['model'] = 'chatglm_lite'
        if 'max_tokens' in config.completion_api_params:
            del config.completion_api_params['max_tokens']

