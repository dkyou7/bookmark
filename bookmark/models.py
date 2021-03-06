from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    # site_name, url은 '필드'라는 용어로 불린다.
    # 동작하기 위해서는 settings.py 에 설정을 추가해주어야 한다.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 관리자 화면에서 출력할 때 나타나는 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])