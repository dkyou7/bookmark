[toc]

# bookmark 서비스 개발

## django framework 사용해보기 2

### 1. init script

```bash
pip install django
django-admin startproject config .
python manage.py migrate
python manage.py createsuperuser
admin
admin@naver.com
1q2w3e4r!@
1q2w3e4r!@
python manage.py runserver

```

- 기본적인 웹 개발 시작하기 위한 설정이 모두 끝났다.

### 2. bookmark app 생성해주기

> python manage.py startapp bookmark

### 3. Make models.py & Set settings.py

>  bookmark/models.py

```python
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    # site_name, url은 '필드'라는 용어로 불린다.
    # 동작하기 위해서는 settings.py 에 설정을 추가해주어야 한다.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 관리자 화면에서 출력할 때 나타나는 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url
```

> config/settings.py

```python
INSTALLED_APPS = [
    'bookmark', # <-- 설정 추가
    ...
]
```

- 데이터베이스 관련 명령이 정상적으로 동작할 것이다.

  > python manage.py makemigrations bookmark

- 마이그레이션 된 파일의 내용을 실제 데이터베이스에 적용시키기 위해

  > python manage.py migrate bookmark

### 4. 관리자 페이지

- 관리자 페이지에 미리 모델을 관리할 수 있도록 등록하자.

```python
from django.contrib import admin
from .models import Bookmark

# Register your models here.
admin.site.register(Bookmark)	# <-- 작성된 모델을 등록해준다.
```

### 5. 뷰 만들기

- 프론트에서 해당 기능을 사용할 수 있도록 만들기

#### 5.1 제네릭 뷰를 사용하여 등록해주자

```python
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
```

- 뷰를 만들었다면, 어떤 주소를 사용해 이 뷰를 호출할 수 있도록 연결해야한다.
- 어떤 주소를 입력시, 해당 페이지를 보여줄 수 있어야 한다.

#### 5.2 url과 뷰를 연결시켜주자

`config/urls.py`

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("bookmark/", include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
```

- `bookmark.urls`에 연동되도록 코딩하였다. 

#### 5.3 해당 url을 설정하자

`bookmark/urls.py`

```python
from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    path('',BookmarkListView.as_view(),name='list'),
]
```

#### 5.4 해당 url을 표현해주는 template를 만들어주자

`bookmark/templates/bookmark/bookmark_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>리스트</title>
</head>
<body>
    <div class="btn-group">
        <a href="#" class="btn btn-info">Add Bookmark</a>
    </div>
    <p></p>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Site</th>
                <th scope="col">URL</th>
                <th scope="col">Modify</th>
                <th scope="col">Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for bookmark in object_list %}
            <br>
                <tr>
                    <td>{{forloop.counter}}</td>
                    <td><a href="#">{{bookmark.site_name}}</a></td>
                    <td><a href="{{bookmark.url}}" target="_blank">{{bookmark.url}}</a></td>
                    <td><a href="#" class="btn btn-success btn-sm">Modify</a></td>
                    <td><a href="#" class="btn btn-danger btn-sm">Delete</a></td>
                </tr>   
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```





