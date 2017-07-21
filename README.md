=====
DRF OAuth Start Kit
=====

一个基于 django-rest-framework 的 oauth 快速搭建工具

Info
-----------
初始化生产 UserProfile 表, 带有 mobile 字段
可以使用 邮箱, 手机号码或用户名(用户只能使用邮箱或手机号进行注册, 注册时生成30位随机数作为用户名)进行登录

Quick start
-----------

<pre>
git clone git@github.com:EvansLyb/tasking.git
cd tasking
virtualenv venv
source vent/bin/activate
pip install -r requirements/common.txt
python manage.py migrate
python manage.py runserver

Cheers!~
</pre>
