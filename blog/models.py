from django.db import models
from django.utils import timezone

#クラス、モデルの定義
class Post(models.Model):
    #プロパティの定義　　　
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #メソッドの定義
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
