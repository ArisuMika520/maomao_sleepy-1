# /client

此目录存储客户端 (用于更新状态/设备状态)

- [/client](#client)
  - [CMDConsole](#cmdconsole)
  - [CmdConsoleMuiti](#cmdconsolemuiti)
  - [WinDevice](#windevice)
  - [BrowserScript](#browserscript)
  - [Other repos](#other-repos)

> [!TIP]
> 欢迎提交 Issue / PR 贡献自己的脚本！

## [CMDConsole](./cmd_console.py)

> by: [@wyf9](https://github.com/wyf9)

一个简单的命令行客户端，用于手动更新状态

依赖: `requests`

## [CmdConsoleMuiti](./cmd_console_muiti.py)

> by: [@wyf9](https://github.com/wyf9)

[CMDConsole](#cmdconsole) 的旧版本 (可选择多个服务)

## [WinDevice](./win_device.py)

> by: [@wyf9](https://github.com/wyf9)

在 Windows 上自动更新设备状态

依赖: `requests`, `pywin32`

> 文件 [L12-L19](https://github.com/wyf9/sleepy/blob/main/client/win_device.py#L12-L19) 的配置如下：

```py
# --- config start
# 服务地址, 末尾同样不带 /
SERVER = 'http://localhost:9010'
# 密钥
SECRET = 'wyf9test'
# 检查间隔，以秒为单位
CHECK_INTERVAL = 2
# 是否忽略重复请求，即窗口未改变时不发送请求
BYPASS_SAME_REQUEST = True
# 设备标识符，唯一 (它也会被包含在 api 返回中, 不要包含敏感数据)
DEVICE_ID = 'device-1'
# 前台显示名称
DEVICE_SHOW_NAME = 'MyDevice1'
# --- config end
```

> PM2 启动命令参考: `pm2 start python --name sleepywin -- -u win_device.py` **(不加 `-u` 参数会导致 `pm2 log` 命令没有输出)**

## [BrowserScript](./页面标题上报脚本-2024.12.2.user.js)

> by: [@nuym](https://github.com/nuym)

在任何支持油猴脚本的浏览器均可使用

- [点击安装 (GitHub raw)](https://raw.githubusercontent.com/wyf9/sleepy/main/client/页面标题上报脚本-2024.12.2.user.js)

- [点击安装 (ghp.ci)](https://ghp.ci/https://raw.githubusercontent.com/wyf9/sleepy/main/client/页面标题上报脚本-2024.12.2.user.js)

> 文件 [L19-L25](https://github.com/wyf9/sleepy/blob/main/client/页面标题上报脚本-2024.12.2.user.js#L19-L25) 的配置如下:

```js
// 参数配置开始
const API_URL = 'https://sleepy.wyf9.top/device/set'; // 你的完整 API 地址，以 `/device/set` 结尾
const SECRET = '绝对猜不出来的密码'; // 你的 secret
const ID = '114514'; // 你的设备 id
const SHOW_NAME = '设备名称'; // 替换为你的设备名称
// [!!!] 请在第 10 行 `@connect` 处的域名改为你的服务域名
// 如本示例中域名就应为 sleepy.wyf9.top
// 参数配置结束
```

## Other repos

> Forks 中发现的脚本，可能需要进行修改以与本分支适配, 见 [API #device-set](../doc/api.md#device-set)

- [1812z/sleepy] Android Macrodroid: [(main) `前台应用状态.macro`](https://github.com/1812z/sleepy/blob/main/%E5%89%8D%E5%8F%B0%E5%BA%94%E7%94%A8%E7%8A%B6%E6%80%81.macro)
- [HBWuChang/sleepy] Android Magisk: [(main) `_example/win.py`](https://github.com/HBWuChang/sleepy/blob/main/_example/win.py) *(详见脚本同目录下 `/magisk`)*
- [HBWuChang/sleepy] Windows Python: [(main) `_example/win.py`](https://github.com/HBWuChang/sleepy/blob/main/_example/win.py)