from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    post_img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name="Изображение")
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.post_img

    def bit(self):
        if self.post_img:
            return u'<img src="%s" width="70"/>' % self.post_img.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True


class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    approwed_article = models.BooleanField(default=True)
    article_img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.article_img

    def bit(self):
        if self.article_img:
            return u'<img src="%s" width="70"/>' % self.article_img.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True


class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    approwed_comment = models.BooleanField(default=False)

    def approve(self):
        self.approwed_comment = True
        self.save()

    def __str__(self):
        return self.text


class Photos(models.Model):
    Photo = models.BooleanField(default=True)
    Slider_Up = models.BooleanField(default=False)
    Slider_Down = models.BooleanField(default=False)
    photo_img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name="Изображение")
    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.photo_img

    def bit(self):
        if self.photo_img:
            return u'<img src="%s" width="70"/>' % self.photo_img.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True


class Orders(models.Model):
    author = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author