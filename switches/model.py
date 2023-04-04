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

    @staticmethod
    def disable():
        """禁用此开关"""
        raise NotImplementedError
