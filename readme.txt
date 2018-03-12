环境部署方法：
1.安装Python2.7版本
2.安装selenium：
   1)命令行方式进入selenium-3.8.1目录
   2)运行python setup.py install，安装selenium驱动
3.下载Chrome driver
   (目录support中已经将Chrome driver下载好)
4.解压zip中的chromedriver.exe
5.拷贝到Chrome的安装目录下...\Google\Chrome\Application\
  例如：C:\Program Files (x86)\Google\Chrome\Application
6.把以上的Chrome安装目录添加到环境变量PATH中

7.更新Chrome浏览器到64版本

8.运行DriverTest.py程序，如果Chrome浏览器被启动，证明环境部署OK。

简历配置方法：
1.打开config文件下的config.ini
2.配置对应站点的网址、用户名、密码、登录时的控件、发帖时的控件
  a.控件识别支持三种类型，ID、CSS、XPATH
  b.配置时，分别写明类型和具体的控件标识，例如：element_passwd = ID , u_login_passwd
3.配置发帖的数量和对应的JD信息
  a.打开北邮人论坛的配置byr.ini
  b.count = 10代表发10个JD信息
  c.其中[1]代表第一个发帖，下面的filepath代表发帖的内容
  d.打开filepath下的内容
    i.第一行是发帖的地址
	ii.第二行是发帖的标题
	iii.第三行是发帖的具体内容