from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost


# 注册插件
@register(name="Switcher", description="快捷切换使用的模型", version="0.1", author="RockChinQ")
class HelloPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(PersonCommandSent)
    @on(GroupCommandSent)
    def process_command(self, event: EventContext, **kwargs):
        pass

    # 插件卸载时触发
    def __del__(self):
        pass
