# sleepy

一个 ~~用于视奸~~ 查看个人在线状态 (以及正在使用软件) 的 Flask 网站，让他人能知道你不在而不是故意吊他/她

[**功能**](#功能) / [**TODO**](#todo) / [演示](#preview) / [**部署**](#部署) / [**使用**](#使用) / [**关于**](#关于)

## 功能

- 自行设置在线状态
- 实时更新设备打开应用 (名称)
- 美观的展示页面 [见 [Preview](#preview)]

### TODO

- [x] Windows 客户端 (Python)
- [ ] Android 客户端
- [ ] 多设备调用
- [ ] 页面丰富/跳转


### Preview

个人演示站: [www.arisumika.cloud](http://www.arisumika.cloud:9010/)

原作者[@wyf9](https://github.com/wyf9)演示站 (稳定): [sleepy.wyf9.top](https://sleepy.wyf9.top)

原作者[@wyf9](https://github.com/wyf9)开发预览 (*不保证可用*, 密钥 `wyf9test`): [sleepy-preview.wyf9.top](https://sleepy-preview.wyf9.top)

## 部署

> 从旧版本更新? 请看 [config.json 更新记录](./doc/config_json_update.md) <br/>
> *配置文件已从 `data.json` 更名为 `config.json`*

理论上全平台通用, 安装了 Python >= **3.6** 即可 (建议: **3.10+**)

1. Clone 本仓库 (建议先 Fork / Use this template)

```shell
git clone https://github.com/wyf9/sleepy.git
```

2. 安装依赖

```shell
pip install flask pytz
```

3. 编辑配置文件

先启动一遍程序:

```shell
python3 server.py
```

如果不出意外，会提示: `config.json not exist, creating`，同时目录下出现 `config.json` 文件，编辑该文件中的配置后重新运行即可 (示例请 [查看 `example.jsonc`](./example.jsonc) )

## 使用

有两种启动方式:

```shell
# 直接启动
python3 server.py
# 简易启动器
python3 start.py
```

默认服务 http 端口: `9010` *(可在 `config.json` 中修改)*

## 客户端示例

如果你想直接开始使用，可在 [`/clients`](./client/README.md) 找到客户端 (用于手动更新状态/自动更新设备打开应用)

## API

详细的 API 文档见 [doc/api.md](./doc/api.md).

## 关于

本项目由[@wyf9](https://github.com/wyf9) 基于灵感来源 Bilibili UP [@WinMEMZ](https://space.bilibili.com/417031122) 而来: [site](https://maao.cc/sleepy/) / [blog](https://www.maodream.com/archives/192/), 并~~部分借鉴~~使用了前端代码, 在此十分感谢。

感谢 [@wyf9](https://github.com/wyf9) 的 源代码提供基本功能框架 [site](https://github.com/wyf9/sleepy)

感谢 [@1812z](https://github.com/1812z) 的 B 站视频推广~ ([BV1LjB9YjEi3](https://www.bilibili.com/video/BV1LjB9YjEi3))

推荐阅读: [HelloFlask (Flask 入门教程)](https://tutorial.helloflask.com/)
