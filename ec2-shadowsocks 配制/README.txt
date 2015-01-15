http://teddysun.com/342.html

一健安装
ec2上
要改
{
    "server":"172.31.9.77",//这里要改成私有ip
    "server_port":8887,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"",
    "timeout":600,
    "method":"aes-256-cfb",
    "fast_open":false,
    "workers":1
}
这里server 抓取到的是ec2上的公有ip
公有ip里还有很好机子. 所以不是公有ip.应改为私有ip.


重启后不能运行
sudo vim /etc/rc.local

加上自启动代码
nohu /usr/local/bin/ssserver -c /etc/shadowsocks/config.json


成功运行


在bwg上安装shadowsocks

http://blog.wifizoo.net/?post=370


1.apt-get install python-gevent python-pip

2. pip install shadowsocks

找到shadowsocks文件夹： sudo find / -name shadows*

在此文件夹下面创建config.json配置文件。

修改config.json

{
    "server":"my_server_ip",
    "server_port":443,
    "local_port":1080,
    "password":"password",
    "timeout":600,
    "method":"aes-256-cfb"
}

另外 要注意的是 如果服务器没有安装m2crypto 需安装否则运行ssserver会报错：M2Crypto is required to use encryption other than default method

安装命令  
apt-get install m2crypto  swig  python-m2crypto

然后切换到配置文件的目录cd /usr/local/lib/python2.7/dist-packages/shadowsocks执行ssserver即可

要注意的是 服务程序需要后台运行 所以开个screen切换到配置文件目录/usr/local/lib/python2.7/dist-packages/shadowsocks运行ssserver就好了。

#:/usr/local/lib/python2.7/dist-packages/shadowsocks# ssserver
shadowsocks 1.3.4
2014-03-07 18:29:55 INFO     loading config from config.json
2014-03-07 18:29:55 INFO     loading config from config.json
2014-03-07 18:29:55 INFO     starting server at *.*.*.*:8388

加入自启动代码
nohup /usr/local/bin/ss-server -c /etc/shadowsocks/config.json > /dev/null 2>&1

多端口配制
{
    "server":"104.224.157.159",
    "local_port":1080,
    "port_password":
    {
        "443":"password1",
        "22":"password2",
        "80":"password3"
    },
    "timeout":600,
    "method":"aes-256-cfb"
}
~
~




服务端配置完毕。