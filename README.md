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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
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
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('',BookmarkListView.as_view(),name='list'),
    path('add/',BookmarkCreateView.as_view(),name="add"),
    path('detail/<int:pk>/',BookmarkDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',BookmarkUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
```

#### 5.4 해당 url을 표현해주는 template를 만들어주자

`bookmark/templates/bookmark/bookmark_list.html`

`bookmark/templates/bookmark/bookmark_create.html`

`bookmark/templates/bookmark/bookmark_confirm_delete.html`

`bookmark/templates/bookmark/bookmark_detail.html`

`bookmark/templates/bookmark/bookmark_update.html`

### 6. 북마크 추가, 수정, 삭제 기능 구현

1. bookmark/views.py 구현
2. bookmark/urls.py 연동
3. 해당 url을 표현해주는 template 구현

### 7. 디자인 입히기

#### 7.1 template 확장하기, 구조 변경하기

1. `templates/base.html` 로 전체 navigation 입히기
2. 각각의 template 들을 알맞게 수정해주자.

#### 7.2 Bootstrap 사용하기

#### 7.3 헤더, 페이지네이션 사용하기

> paginate_by = 3

- 페이지네이션을 지원하는 django 기능이다...
- 몇개 단위로 끊을 것인지 알려준다.

### 8. 정적 파일 사용해서 CSS 꾸미기

1. `static/style.css`파일 만들기

2. `config/settings.py` 맨 밑에

   > ```python
   > STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
   > ```

   추가

### 9. 베포하기

- 깃허브 업로드, 파이썬 애니웨어에서 소스코드를 깃 명령을 이용해 다운
- 몇가지 셋팅 후 베포 완료

#### 9.1 소스 코드 업로드

- `.gitignore`

```python
*.pyc
*~
/venv
__pycache__
db.sqlite3
.DS_Store
```

- `settings.py`

```python
DEBUG = False

ALLOWED_HOSTS = ['*']
```

#### 9.2 git 에 업로드

#### 9.3 pythonanywhere 에 git 파일 업로드

- 회원 가입

- bash

  ```
  pwd
  git clone ~~~.git
  cd bookmark
  virtualenv venv --python=3.7
  source venv/bin/activate
  pip install django
  python manage.py migrate
  python manage.py createsuperuser
  ```

- 웹 앱 생성 후 WSGI 설정

