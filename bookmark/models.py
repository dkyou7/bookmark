from django.db import models

# Create your models here.
class Bookmark(models.Model):
    # site_name, url은 '필드'라는 용어로 불린다.
    # 동작하기 위해서는 settings.py 에 설정을 추가해주어야 한다.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')