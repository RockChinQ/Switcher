from .model import AbstractSwitch


class HugChat(AbstractSwitch):
    "HuggingChat的开关"

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "HuggingChat"

    @staticmethod
    def get_alias() -> str:
        return "hugchat"

    @staticmethod
    def supported() -> bool:
        from pkg.plugin.host import __plugins__
        if 'revLibs' in __plugins__:
            try:
                from plugins.revLibs.pkg.process.impls.hugchat import HugChatImpl
                return True
            except:
                return False
        else:
            return False

    @staticmethod
    def enable():
        from pkg.plugin.host import __plugins__
        __plugins__['revLibs']['enabled'] = True
        import revcfg
        setattr(revcfg, 'reverse_lib', 'Soulter/hugging-chat-api')

        from plugins.revLibs.pkg.process.impls.hugchat import HugChatImpl
        import plugins.revLibs.pkg.process.revss
        plugins.revLibs.pkg.process.revss.__rev_interface_impl_class__ = HugChatImpl
        plugins.revLibs.pkg.process.revss.__sessions__ = {}