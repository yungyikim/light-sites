from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    subject = models.CharField(
        max_length=128,
        null=False,
        help_text='게시물 제목'
    )
    description = models.TextField(
        null=True,
    )
    content = models.TextField(
        null=True,
        help_text='HTML형태의 게시물 내용'
    )
    thumbnail = models.CharField(
        max_length=255,
        null=True,
        help_text='썸네일 이미지 URL'
    )
    create_date = models.DateTimeField(
        auto_now_add=False,
        db_index=True
    )
    modified_date = models.DateTimeField(
        auto_now_add=False
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '%s' % self.id
