# 简介

函数计算文档示例代码

# 如何新开发一个 3.0 的应用

## 1. 初始化一个应用

假设您想要的生成一个 nodejs 的 hello world 代码示例，您可以执行以下命令：

```bash
s init start-application-v3 -d  nodejs_hello_world
```

执行成功后会生成 nodejs_hello_world 目录

## 2. 进入 nodejs_hello_world 目录进行组件开发

| 目录         | 含义                                                     |
| ------------ | -------------------------------------------------------- |
| readme.md    | 对该组件的描述，或帮助文档信息                           |
| version.md   | 版本的描述，例如当前版本的更新内容等                     |
| publish.yaml | 项目所必须的文件，Serverless Devs Package 的开发识别文档 |
| src          | 应用所在目录，需要包括`s.yaml`和相关的应用代码等         |

此时，开发者可以在 src 下完成应用的开发，并对项目进行`publish.yaml`文件的编写。完成之后，即可通过以下几个步骤发布项目：

- 更改 `publish.yaml` 里的 `Name` 字段，给自己的应用取一个名字，分类和 Service 参考注释中的 https://api.devsapp.cn/v3/common/args.html

- 更改 `publish.yaml` 里的 `Version` 字段为 dev

- 取消掉 `publish.yaml` 里的 `Organization` 注释

  > 默认的模版中 publish.yaml 中的 "Organization: 阿里云函数计算（FC）" 是注释掉的， 如果取消注释的话，设置应用属于阿里云函数计算（FC）组织的话， 执行 `s registry login`, 完成 github 授权登录，然后把 github 名字告诉江昱或者西流后台添加下到对应的组织才有权限发布

- 在 publish.yaml 所在的目录上执行 `s cli alireadme3` 完成应用 readme 的编写

  > readme_en.md 可以可删除不考虑

- 首次发布需要通过 [registry](https://docs.serverless-devs.com/serverless-devs/command/registry) 命令先登录 Serverless Devs Registry。

  ```bash
  s registry login
  ```

  随后浏览器会跳出登陆窗口，根据提示进行操作即可。

- 后续直接执行 `s registry publish` 即可进行发布

- 测试应用

  如果您使用 dev 版本进行了应用的发布， 假设您的应用名字为 start-application-v3, 那么您可以使用：

  - 本地终端执行: `s init start-application-v3@dev`
  - 浏览器打开: https://fcnext.console.aliyun.com/applications/create?template=start-application-v3@dev 进行测试

- 发布正式版本

  更改 `publish.yaml` 里的 `Version` 字段为 0.0.1, 确保版本号比现有最高版本号大 1，例如：0.0.1 -> 0.0.2。

## 3. 提交 PR，将您开发的新应用合并 master
