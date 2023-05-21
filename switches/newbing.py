from .model import AbstractSwitch


class NewBing(AbstractSwitch):
    """New Bing的开关"""

    def __init__(self):
        pass

    @staticmethod
    def get_name() -> str:
        return "New Bing"

    @staticmethod
    def get_alias() -> str:
        return "bing"

    @staticmethod
    def supported() -> bool:
        from pkg.plugin.host import __plugins__
        return 'revLibs' in __plugins__

    @staticmethod
    def enable():
        from pkg.plugin.host import __plugins__
        __plugins__['revLibs']['enabled'] = True
        import revcfg
        setattr(revcfg, 'reverse_lib', 'acheong08/EdgeGPT')

        from plugins.revLibs.pkg.process.impls.edgegpt import EdgeGPTImpl
        import plugins.revLibs.pkg.process.revss
        plugins.revLibs.pkg.process.revss.__rev_interface_impl_class__ = EdgeGPTImpl
        plugins.revLibs.pkg.process.revss.__sessions__ = {}
