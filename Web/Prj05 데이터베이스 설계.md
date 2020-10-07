# Prj05 데이터베이스 설계

- **목표**
  - 데이터를 생성, 조회, 수정, 삭제 할 수 있는 Web Application 제작
  - Python Web Framework를 통한 데이터 조작
  - Authentication에 대한 이해
  - Database 1:N에 대한 이해와 데이터 관계 설정



- **요구사항**

  커뮤니티 서비스의 회원관련 기능 개발을 위한 단계로, 모델간의 관계 설정 후 데이
  터의 생성, 조회, 수정, 삭제 할 수 있는 기능을 완성합니다. 해당 기능은 향후 커뮤니
  티 서비스의 필수 기능으로 사용됩니다.

  A. 프로젝트 구조

  - pjt05/은 startproject 명령어로 생성되는 project 디렉토리입니다.
  - community/는 startapp 명령어로 생성되는 application 디렉토리입니다.

  - 간단히 가상환경설정과 .gitignore 등의 설정을 마치고 아래와 같이 프로젝트와 앱을 만들어 주었다

  ```bash
  $ django-admin startproject pjt05 .
  $ python manage.py startapp community
  $ python manage.py startapp accounts
  ```

  B. Model

  데이터베이스에서 모델의 ERD(Entity Relation Diagram)는 아래와 같습니다.

  ![image-20201007192537887](C:/Users/82108/Desktop/pjt05/pjt05/README.assets/image-20201007192537887.png)

  ​	

  - 위와 같은 모델을 만들기 위해 아래와 같이 모델링을 해주고, 여기서 rank의 범위를 제한하기 위해 새로 정의한 부분들은 뒤에 설명하겠다

    ```python
    # accounts/models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    class User(AbstractUser):
        pass
    
    # community/models.py
    from django.db import models
    from django.conf import settings
    from django.core.validators import MinValueValidator, MaxValueValidator
    
    
    class IntegerRangeField(models.IntegerField):
        def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
            self.min_value, self.max_value = min_value, max_value
            models.IntegerField.__init__(self, verbose_name, name, **kwargs)
        def formfield(self, **kwargs):
            defaults = {'min_value': self.min_value, 'max_value':self.max_value}
            defaults.update(kwargs)
            return super(IntegerRangeField, self).formfield(**defaults)
    
    
    class Review(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        movie_title = models.CharField(max_length=50)
        rank = IntegerRangeField(min_value=0, max_value=5)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.title
    
    
    class Comment(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        review = models.ForeignKey(Review, on_delete=models.CASCADE)
        content = models.CharField(max_length=100)
    
        def __str__(self):
            return self.content
    ```

  C. **Form**

  - Review, Comment의 데이터 검증, 저장, 에러메세지, HTML을 모두 관리하기 위해
    ModelForm을 사용합니다.
  - User의 데이터 검증, 저장, 에러메세지, HTML을 모두 관리하기 위해 django에서
    제공하는 ModelForm, Form을 사용합니다.
  - 아래와 같이 Form또 customize해서 작성해준다.

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm, UserCreationForm
  from django.contrib.auth import get_user_model
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
  
          
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields
          
  # community/forms.py
  from django import forms
  from .models import Review, Comment
  
  class ReviewForm(forms.ModelForm):
      # rank = forms.IntegerField(
      #     widget=forms.IntegerField(max_value=5)
      # )
  
      class Meta:
          model = Review
          exclude = ['user',]
  
  
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          fields = ['content',]
  ```

  D. Admin

  - Review, Comment는 관리자 페이지에서 데이터의 생성, 조회, 수정, 삭제 가능해
    야 합니다.
  - (Admin 페이지에서 테스트 목적으로 데이터를 생성, 조회, 수정, 삭제
    할 수 있습니다.

  ```python
  # accounts/admin.py
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  admin.site.register(User, UserAdmin)
  
  # community/admin.py
  from django.contrib import admin
  from .models import Review, Comment
  # Register your models here.
  
  admin.site.register(Review)
  admin.site.register(Comment)
  ```

  E. URL

  - 각각의 URL을 아래와 같이 연결을 해주었다

    ![image-20201007193240960](C:/Users/82108/Desktop/pjt05/pjt05/README.assets/image-20201007193240960.png)

  ```python
  # pjt05/urls.py
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('accounts/', include('accounts.urls')),
      path('community/', include('community.urls')),
  ]
  
  # accounts/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
      path('login/', views.login, name='login'),
      path('logout/', views.logout, name='logout'),
  ]
  
  # community/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'community'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:review_pk>/', views.detail, name='detail'),
      path('<int:review_pk>/comments/', views.create_comment, name='create_comment'),
      path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
  ]
  ```

  F. View & Template

  - 프로젝트폴더 settings.py에서 BASE_DIR 설정을 해주고

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/ 'pjt05' / 'templates'],
            ...
    
        },
    ]
    ```

  - 간단하게 base.html도 작성해 주었다

  - Navbar을 이용한 페이지들 연결

  - 로그인 했을시엔 아래와 같이

    ```html
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            {% if request.user.is_authenticated %}
            <a class="navbar-brand" href="{% url 'community:index'%}">{{ user }}</a>
                <div class="justify-content-end collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav mx-3">
                    <div class="d-flex align-items-center">
                        <li class="nav-item mx-1">
                            <a class="nav-link" href="{% url 'community:index' %}">REVIEWS</a>
                        </li>
                        <li class="nav-item mx-1">
                            <a class="nav-link" href="{% url 'community:create' %}">NEW REVIEW</a>
                        </li>
                        <li class="nav-item mx-1">
                            <form action="{% url 'accounts:logout' %}" method="POST">
                                {% csrf_token %}
                                <input type="submit" value="LOGOUT">
                            </form>
                        </li>
                    </div>
                    </ul>
                </div>
            {% else %}
    
    
    ```

  ![image-20201007194252340](C:/Users/82108/Desktop/pjt05/pjt05/README.assets/image-20201007194252340.png)

  - 로그인 하지 않은 상태에선 아래와 같이 기본 페이지를 만들어주었다.

    ```html
            <a class="navbar-brand" href="{% url 'community:index'%}">COMMUNITY</a>
                <div class="justify-content-end collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav mx-3">
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="{% url 'community:index' %}">REVIEWS</a>
                    </li>
                     <li class="nav-item mx-1">
                        <a class="nav-link" href="{% url 'community:create' %}">NEW REVIEW</a>
                    </li>
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="{% url 'accounts:login' %}">LOGIN</a>
                    </li>
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="{% url 'accounts:signup' %}">SIGNUP</a>
                    </li>
                    </ul>
                </div>
            {% endif %}
    
            
        </nav>
        <div class="container">
        {% block content %}
        {% endblock %}
        </div>
    ```

    ![image-20201007194236679](C:/Users/82108/Desktop/pjt05/pjt05/README.assets/image-20201007194236679.png)

  - Accounts에서 Login, Signup, Logout 에 대한 views.py 생성

  ```python
  # accounts/views.py
  from django.shortcuts import render, redirect
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as auth_logout
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
  from django.views.decorators.http import require_http_methods, require_POST
  from .forms import CustomUserChangeForm, CustomUserCreationForm
  
  # Create your views here.
  @require_http_methods(['GET', 'POST'])
  def signup(request):
      if request.user.is_authenticated:
          return redirect('community:index')
  
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('community:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  
  
  @require_http_methods(['GET', 'POST'])
  def login(request):
      if request.user.is_authenticated:
          return redirect('community:index')
  
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect(request.GET.get('next') or 'community:index')
      else:
          form = AuthenticationForm()
      context = {
          'form' : form,
      }
      return render(request, 'accounts/login.html', context)
  
  @require_POST
  def logout(request):
      auth_logout(request)
      return redirect('community:index')
  ```

  - 이에 이어 간단하게 template들도 각각 작성했다

  ```html
  {% comment %} accounts/login.html {% endcomment %}
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>LOGIN</h1>
  <hr>
  <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
  </form>
  <a href="{% url 'community:index' %}">[BACK]</a>
  {% endblock %}
  
  {% comment %} accounts/signup.html {% endcomment %}
  {% extends 'base.html' %}
  
  {% block content %}
  <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
  </form>
  <a href="{% url 'community:index' %}">[BACK]</a>
  {% endblock %}
  ```

  ---

  여기까지는 큰 문제가 없이 진행이 되었고, 주어진과제의 전부였다. Bootstrap을 이용한 styling은 같은 팀원인 이승아님이 아주 깔끔하게 해주셨다.

  프로젝트시간이 끝나고, 아래에 조금 더 추가를 하면서 구현하고 바꾼 내용을 적어보았다.