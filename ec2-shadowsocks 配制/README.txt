http://teddysun.com/342.html

һ����װ
ec2��
Ҫ��
{
    "server":"172.31.9.77",//����Ҫ�ĳ�˽��ip
    "server_port":8887,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"",
    "timeout":600,
    "method":"aes-256-cfb",
    "fast_open":false,
    "workers":1
}
����server ץȡ������ec2�ϵĹ���ip
����ip�ﻹ�кܺû���. ���Բ��ǹ���ip.Ӧ��Ϊ˽��ip.


������������
sudo vim /etc/rc.local

��������������
nohu /usr/local/bin/ssserver -c /etc/shadowsocks/config.json


�ɹ�����


��bwg�ϰ�װshadowsocks

http://blog.wifizoo.net/?post=370

0.apt-get update
1.apt-get install python-gevent python-pip

2. pip install shadowsocks
apt-get install m2crypto  swig  python-m2crypto
mkdir /etc/shadowsocks
cd /etc/shadowsocks
vi config.json

�ڴ��ļ������洴��config.json�����ļ���

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






�����������ϡ�