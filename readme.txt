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