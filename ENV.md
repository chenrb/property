# 需要配置的环境变量

目标运行环境：Python 3.14 + Django 6.0.x。

DJANGO密钥：SECRET_KEY

本地开发可以使用 `.\env.cmd` 或 `config/local_settings.py` 设置
`SECRET_KEY`。运行测试且未设置 `SECRET_KEY` 时，项目会使用仅限测试的默认
密钥；生产和普通开发运行必须通过环境变量或本地配置文件设置真实密钥。
