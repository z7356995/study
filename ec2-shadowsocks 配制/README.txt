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

0.apt-get update
1.apt-get install python-gevent python-pip

2. pip install shadowsocks
apt-get install m2crypto  swig  python-m2crypto
mkdir /etc/shadowsocks
cd /etc/shadowsocks
vi config.json

在此文件夹下面创建config.json配置文件。

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

nohup /usr/local/bin/ssserver -c /etc/shadowsocks/config.json > /dev/null 2>&1






服务端配置完毕。