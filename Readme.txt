1. 进入到这个目录
2. 执行“python manage.py runserver 127.0.0.1:8000” （windows需要进入cmd执行）
3. 然后浏览器里面输入 http://127.0.0.1:8000/admin/
4. 第一次进入需要登陆，数据库里已经有admin/admin这个管理员了
   4.1 如果需要再创建管理员，则执行python manage.py createsuperuser
5. 进去之后，就可以看到管理后台，管理用户和图书

6. 除了admin这块，其他功能，需要先注册再登录
1） http://127.0.0.1:8000/signup/
填写信息，然后注册
2）http://127.0.0.1:8000/login/
填写信息，然后登录
3）接着就可以访问其他的接口了
