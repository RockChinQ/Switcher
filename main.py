from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost


def reset_to_default():
    # 检查是否要关闭逆向库插件
    from pkg.plugin.host import __plugins__
    if 'revLibs' in __plugins__:
        __plugins__['revLibs']['enabled'] = False

    # 重置到默认的gpt-3.5模型
    import config
    config.completion_api_params['model'] = 'gpt-3.5-turbo'


# 注册插件
@register(name="Switcher", description="快捷切换使用的模型", version="0.1", author="RockChinQ")
class SwitcherPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        from .switches.model import register_all
        register_all()

    @on(PersonCommandSent)
    @on(GroupCommandSent)
    def process_command(self, event: EventContext, **kwargs):
        params = kwargs['params']
        cmd = kwargs['command']

        from .switches.model import __switches__

        if cmd == 'switch':
            event.prevent_default()
            event.prevent_postorder()
            if kwargs['is_admin']:
                if len(params) == 0:
                    # 输出所有可用模型
                    reply_str = "[Switcher] 已支持切换的模型：\n\n"
                    for key in __switches__:
                        switch = __switches__[key]
                        if switch.supported():
                            reply_str += f"{switch.get_alias()} - {switch.get_name()}\n"
                    reply_str += "\n请输入 !switch <模型别名> 进行切换, 例如: !switch gpt3.5"
                    event.add_return('reply', [reply_str])
                else:
                    # 切换模型
                    alias = params[0]
                    if alias in __switches__:
                        switch = __switches__[alias]
                        if switch.supported():
                            reset_to_default()
                            switch.enable()
                            event.add_return('reply', [f"[Switcher] 已切换至 {switch.get_name()}"])
                        else:
                            event.add_return('reply', [f"[Switcher] 模型 {switch.get_name()} 不支持当前环境"])
                    else:
                        event.add_return('reply', [f"[Switcher] 未找到模型 {alias}"])
            else:
                event.add_return('reply', ["[Switcher] 您不是管理员，无法使用此命令"])

    # 插件卸载时触发
    def __del__(self):
        pass
