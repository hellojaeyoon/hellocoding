# 2020.09.14(월) - Django Recap

* **가상환경 생성 및 진입**

  ```bash
  # 가상환경 생성
  $ python -m venv venv
  
  # 가상환경 진입
  $ source venv/Scripts/activate  # Windows
  $ source venv/bin/activate      # Mac
  ```

* **django 설치**

  ```bash
  $ pip install django
  ```

* **프로젝트 생성 및 서버 실행**

  ```bash
  # 프로젝트 생성
  $ django-admin startproject django_recap .
  
  # 서버 실행
  $ python manage.py runserver
  ```

* **애플리케이션 생성 및 등록**

  ```bash
  $ python manage.py startapp articles
  ```

  ```python
  # django_recap/settings.py
  
  INSTALLED_APPS = [
      'articles',
      ...
  ]
  ```

* **기타 환경 설정**

  ```python
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  ```

* **URL 분리**

  ```python
  # django_crud/urls.py
  urlpatterns = [
      path('admin/', admin.site.urls),
      # 'articles/'로 시작하는 주소는 articles 앱의 urls.py에서 처리
      path('articles/', include('articles.urls')),  
  ]
  ```

  ```python
  # articles/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  urlpatterns = [
      
  ]
  ```

* **DB 모델링 (`models.py`)**

  ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=50)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

* **마이그레이션**

  ```bash
  # 설계도 파일 만들기
  $ python manage.py makemigrations
  
  # 설계도 데이터베이스 반영 상태 확인하기
  $ python manage.py showmigrations
  
  # 설계도를 실제 데이터베이스에 반영하기
  $ python manage.py migrate
  ```

* **템플릿 상속**

  * 장고는 템플릿을 찾을 때 기본적으로 INSTALLED_APPS에 등록해둔 앱을 순서대로 방문하면서, 앱 안에 있는 templates 폴더를 탐색한다.
  * 프로젝트 폴더에 있는 base.html 파일을 찾게 하기 위해 템플릿 경로를 수정한다.

  ```python
  # django_recap/settings.py
  
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'django_recap' / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  ```html
  <!-- django_recap/templates/base.html -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>
      Django Recap - 
      {% block title %}
      {% endblock %}
    </title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
  </html>
  ```
	```python
	# articles/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  
  # articles/views.py
  from django.shortcuts import render
  
  # Create your views here.
  def index(request):
      return render(request, 'articles/index.html')

  ```
  ```html
  <!-- articles/templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block title %}
  Main
  {% endblock %}
  
  {% block content %}
  <h1 class="text-center">Articles</h1>
  <hr>
  {% endblock %}
  ```
  
  



