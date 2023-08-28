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





