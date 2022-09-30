# Django Tutorial

## 1. [Django官方网站](https://www.djangoproject.com/)

## 2. Django特点
- DRY (Do Not Repeat Yourself) 原则
- 采用MTV框架（即模型Model、模版Template、视图View），同时也遵循MVC

## 3. 常用命令
- 创建工程   
```django-admin startproject 你的工程名称(myshop)```
- 创建应用   
```python/python3 manage.py startapp 你的app名(app1)```
- 启动项目  
```python/python3 manage.py runserver 0.0.0.0:8000```

## 4. 术语
- project&app  
一套目录结构和其中的设置就是一个Django可识别的项目。
应用指的就是一组Model（数据模型）、Views（视图）、Templates（模板）和URLs的集合。
Django框架通过使用应用，为站点提供各种功能，应用还可以被复用在不同的项目中。你可以将一个项目理解为一个站点，站点中包含很多功能，比如博客，wiki，论坛，每一种功能都可以看作是一个应用。

## 5. [csrf](https://www.youtube.com/watch?v=gEPii2y3ISQ)
csrf防御
- 尽量使用post
- 加入验证码
- 验证Referer
- Anti CSRF Token

## 6. [ajax](https://www.runoob.com/php/php-ajax-intro.html)
AJAX = Asynchronous JavaScript and XML.

AJAX 是一种用于创建快速动态网页的技术。

AJAX 通过在后台与服务器进行```少量数据```交换，使网页实现```异步更新```。这意味着可以在不重载整个页面的情况下，对网页的某些```部分进行更新```。

传统的网页（不使用AJAX）如果需要更新内容，必须重载整个页面。