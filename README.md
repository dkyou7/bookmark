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

