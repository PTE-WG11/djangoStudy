## 1、setting
一、数据库已修改成mysql

二、时区修改成中国 ：TIME_ZONE = 'Asia/Shanghai'
中文：LANGUAGE_CODE = 'zh-hans'

三、创建用做练习的应用app1：
pytthon manage.py startapp app1

四、STATIC_URL = '/static/'
app下的static在上述配置完成后是可以正常使用的
设置根目录静态文件夹
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

五、设置App（app1）的静态资源文件夹static1：
os.path.join(BASE_DIR,'app1/static1'))

## 2、路由
一、大路由（include），小路由（path）
二、路由变量
三、re_path<正则表达式>
## 3、GET--POST
##4、MTV＿T（模板）
setting: 
BACKEND：指定模板的引擎
DIRS:模板的搜索目录（一个或多个 ）
APP_DIRS：是否在应用中的templates文件夹中搜索模板文件
OPTIONS：有关的模板的选项
###URL反向解析