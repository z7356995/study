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


1.apt-get install python-gevent python-pip

2. pip install shadowsocks

�ҵ�shadowsocks�ļ��У� sudo find / -name shadows*

�ڴ��ļ������洴��config.json�����ļ���

�޸�config.json

{
    "server":"my_server_ip",
    "server_port":443,
    "local_port":1080,
    "password":"password",
    "timeout":600,
    "method":"aes-256-cfb"
}

���� Ҫע����� ���������û�а�װm2crypto �谲װ��������ssserver�ᱨ��M2Crypto is required to use encryption other than default method

��װ����  
apt-get install m2crypto  swig  python-m2crypto

Ȼ���л��������ļ���Ŀ¼cd /usr/local/lib/python2.7/dist-packages/shadowsocksִ��ssserver����

Ҫע����� ���������Ҫ��̨���� ���Կ���screen�л��������ļ�Ŀ¼/usr/local/lib/python2.7/dist-packages/shadowsocks����ssserver�ͺ��ˡ�

#:/usr/local/lib/python2.7/dist-packages/shadowsocks# ssserver
shadowsocks 1.3.4
2014-03-07 18:29:55 INFO     loading config from config.json
2014-03-07 18:29:55 INFO     loading config from config.json
2014-03-07 18:29:55 INFO     starting server at *.*.*.*:8388

��������������
nohup /usr/local/bin/ss-server -c /etc/shadowsocks/config.json > /dev/null 2>&1

��˿�����
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




�����������ϡ�