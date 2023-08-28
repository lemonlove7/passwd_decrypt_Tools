运行ToDesk后会在默认安装目录下生成一个config.ini配置文件，存储的有设备代码、临时密码、安全密码以及登录用户和密码等重要敏感信息。我们只需要找到todesk的根目录即可，然后查看config.ini，在config.ini可以找到识别码以及加密的密码，即clientid字段和tempAuthPassEx字段

```
[ConfigInfo]
screen_img=
localPort=35600
clientId=767****68
PrivateData=d88f1c6d9a29586481d1d18c97de14ec949c431dec2f382e0cd5f8d47dc486f287664ce1a060c888862dfade939d1d39a27b0b3fe4a83ea5e1
language=936
Version=4.2.9
tempAuthPassEx=77075794f6310ab54fee1e13935e5392771c24c418a6d526e3ab83ef578d215ebd87467876fd7f55312fb8dbbe9c478e35da8a3069a2
updatePassTime=20220512
Resolution=2560x1440
LastPushTimeEx=20220512
autoStart=0
```
对于加密的密码我们可以复制到本地的todesk配置文件里，替换我们本地的密码，然后重启todesk，这样就能得倒对方机器的连接密码
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/0d5c87b8-4306-4226-9f04-40dbd873748c)
成功替换得到密码。
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/3e6a0e6a-919b-4e1e-8096-842d43400170)


