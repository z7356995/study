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
/usr/local/bin/ssserver -c /etc/shadowsocks/config.json


成功运行
