
# php SDK 接入快速上手

- sdk 的用法在 ```main.py``` 里

# 0x00 相关依赖

[![#](https://img.shields.io/badge/python-2.7-green.svg)](https://github.com/lvxunDev/yunhetong-python-sdk)
[![#](https://img.shields.io/badge/pycrypto-2.6.1-blue.svg)](https://github.com/lvxunDev/yunhetong-python-sdk)
[![#](https://img.shields.io/badge/requests-2.12.4-blue.svg)](https://github.com/lvxunDev/yunhetong-python-sdk)


# 0x01 目录结构

```
pythonSDK
|
|-------docs     // 一些说明文档
|-------main.py  // 一些使用示例
|-------lib      // python php SDK 核心包
|         |---- aes.py      // AES 加密相关的一个类，客户一般不需要使用
|         |---- rsa.py      // RSA 加密相关的一个类，客户一般不需要使用
|         |---- sdk_manager.py      // 客户最主要使用的一个类
|         |---- secretManager.py   // 加解密管理类，客户一般不需要调用
```

# 0x02 初始化 LxSDKManager

为了方便，这里我们建一个资源类```resource.py```,并添加如下代码：

``` python

# coding=utf-8
import time

from lib.sdk_manager import SDKManager


class R:

    app_id = "2016121514373700002"
    pub_path = '/pem/yhtSK.pem'
    pri_path = '/pem/rsa_private_key_pkcs8.pem'

    @staticmethod
    def get_sdk_manager():
        """
            get a test SDKManager
        """
        return SDKManager(R.app_id, R.pub_path, R.pri_path)

```
其中公私玥参考公私玥相关的那篇文章。


# 0x03 导入用户
我们要导入用户并且获取 token
- 准备用户数据

在 R 类中添加如下代码

``` python

    @staticmethod
    def get_test_user_a():
    """
    获取测试用户 a
    """
        user_a = {
            'appId': R.app_id,                # 第三方应用的 appId
            'appUserId': 'pythonTestUserA',   # 用户在第三方应用的唯一标识
            'userType': 1,                    # 用户类型,1是个人，2是企业
            'cellNum': '11111111122',         # 电话号码，为1开头的11为数字
            'userName': 'TestB',              # 用户名称
            'certifyType': 2,                 # 实名认证类型，1身份证2护照3军官证4营业执照5组织机构代码证
            'certifyNumber': '52059487',      # 用户实名认证时候的证件号码，可以是对应的身份证、营业执照、组织机构代码证或者其他证件号码，原则上不能大于 30 个字符
            'createSignature': '0'            # 是否自动创建签名，在导入用户并且当值为 1 时，会为导入的用户自动创建签名，0的话就不会，这个值只在用户第一次导入时有效
        }
        return user_a
```

- 导入用户

``` python
    # 首先，初始化 sdk_manager
    sdk_manager = R.get_sdk_manager()
    # 然后随便初始化一个用户信息
    user_a = R.get_test_user_a()
    # 获取这个用户的 token
    print sdk_manager.get_token(user_a) + '\r\n\r\n'
```

- 返回结果
正常会返回如下所示字符串

``` json
{"code":200,"message":"true","subCode":200,"value":{"contractList":[{"id":1701061349385004,"status":"签署中","title":"测试合同标题40"},{"id":1701031046255028,"status":"签署中","title":"测试合同标题25"}],"token":"TGT-31356-4FZDJcQR3yK4IiaWIafnxQY0QAIoAI0SP6jja0VFY65PJ1S2W4-cas01.example.org"}}
```

然后将 token 返回给客户端，客户端再通过这个 token 去调用相应的SDK（比如js SDK 或 Android SDK 或 iOS SDK），去访问合同操作

# 0x04 生成合同
初始化 sdk_manager 略，参考上面第一条。假设有个 A,B 两个人，A 要发起一份合同合同给 B，此时 A是合同的发起方， 也是合同的参与方。以此为例，代码如下
- 准备用户 B 信息
参考上面第二条用户 A 的信息，用户 B 的代码如下

```python

    @staticmethod
    def get_test_user_b():
    """
    获取测试用户b
    """
        user_b = {
            'appId': R.app_id,
            'appUserId': 'pythonTestUserB',
            'userType': 1,
            'cellNum': '11111111122',
            'userName': 'TestB',
            'certifyType': 2,
            'certifyNumber': '52059487',
            'createSignature': '0'
        }
        return user_b
```

- 准备合同信息

``` python
    @staticmethod
    def get_test_contract():
    """
    获取测试合同信息
    """
        contract = {
            "appId" : R.app_id,
            "title" : "测试合同标题",
            "overtime" : int(round(time.time() * 1000)),
            "defContractNo" : "自定义合同标题",
            "templateId" : 123456,
            "params" : R.get_contract_params(),
        }
        return contract

    @staticmethod
    def get_contract_params():
    """
    获取合同占位符
    """
        params = {
            "${nameA}" : "py测试用户名A"
        }
        return params
```
- 准备合同参与方

在刚才的用户A、B的基础上，我们可以生成合同的参与方

``` python

    @staticmethod
    def get_actors():
    """
    获取两个测试的合同参与方
    """
        return (R.actor_a(),R.actor_b())


    @staticmethod
    def actor_a():
    """
    这个是参与方 A
    """
        actor_a = {
            "user" : R.get_test_user_a(),
            "locationName" : "signA",
            "autoSign" : 0
        }
        return actor_a


    @staticmethod
    def actor_b():
    """
    这个是参与方 B
    """
        actor_b = {
            "user" : R.get_test_user_b(),
            "locationName" : "signA",
            "autoSign" : 0
        }
        return actor_b


```

- 生成合同

```python
    # 创建一份合同
    print sdk_manager.create_contract(R.get_test_contract(), R.get_actors()) + '\r\n\r\n'
```

- 返回结果
正常的话会返回如下所示字符串

``` json
{"code":200,"message":"true","subCode":200,"value":{"contractId":1701061352090008}}
```

将上一步得到的 token 和这里的 contractId 返回给客户端，即可用相应的 SDK（比如js SDK 或 Android SDK 或 iOS SDK），去进行合同的相关操作。

# 0x05 通过创建合同获取 token
有时候我们想在创建合同的同时也获取 Token，我们可以像下面这样

``` python
    # 或者你也可以在创建合同的时候顺便获取 token
    print sdk_manager.token_contract(R.get_test_user_a(), R.get_test_contract(), R.get_actors()) + '\r\n\r\n'
```

正常的话会返回如下所示字符串

``` json
{"code":200,"message":"true","subCode":200,"value":{"contractId":1701061349385004,"token":"TGT-31353-vpnotTbYFJ5wXoTUDzjSD9eVqZfzx9RZIsUhqGcEL5kjRcS6V6-cas01.example.org"}}
```


# 0x06 End
就是这么简单方便，嘿嘿嘿~






