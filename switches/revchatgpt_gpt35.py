from .model import AbstractSwitch


class RevChatGPT35(AbstractSwitch):
    """逆向库插件ChatGPT 3.5"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "ChatGPT网页版逆向3.5"

    @staticmethod
    def get_alias() -> str:
        return "rgpt3.5"

    @staticmethod
    def supported() -> bool:
        # 检查是否安装了revLibs插件
        from pkg.plugin.host import __plugins__
        return 'revLibs' in __plugins__

    @staticmethod
    def enable():
        from pkg.plugin.host import __plugins__
        __plugins__['revLibs']['enabled'] = True
        import revcfg
        setattr(revcfg, 'reverse_lib', 'acheong08/ChatGPT.V1')

        from plugins.revLibs.pkg.process.impls.v1impl import RevChatGPTV1
        import plugins.revLibs.pkg.process.revss
        plugins.revLibs.pkg.process.revss.__rev_interface_impl_class__ = RevChatGPTV1
