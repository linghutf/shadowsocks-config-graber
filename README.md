# shadowsocks-config-graber
from the newwork get shadowsocks config,wirte into config.json,yhen you can use it in ss environment.

<<<<<<< HEAD
默认读取kf0.cc 美国节点免费ss信息，该站点4个小时更新
，可以使用cron等工具指定后台更新时间
获取的信息以myconfig1.json 存储在当前目录下
=======
1.Abount
us_shadowsocks.py默认读取kf0.cc 美国节点免费ss信息，该站点4个小时更新
，可以指定后台更新时间
getss.py获取的信息以myconfig1.json,myconfig2.json形式存储在当前目录下

目前使用shadowsocks-nodejs的客户端sslocal -c xxx.json报错，
格式检查了都是正确的，不知道哪里失败了。

2.Requirement
两个脚本都需要python2,并且安装了requests,beautifulsoup4,安装方法如下
pip install requests
pip install beautifulsoup4

Enjoy it!
>>>>>>> origin/master
