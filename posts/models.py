from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from places.models import Place
from users.models import User


class Love(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return str(self.user.pk)


class Post(models.Model):
    user = models.ForeignKey(User, related_name='User_post', on_delete=models.CASCADE)

    body = models.TextField()

    likes = GenericRelation(Love)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=255, default='post')
    index = models.IntegerField(default=0,null=True,blank=True)
    img = models.ImageField(upload_to='posts', blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return str(self.user)


class Attachment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.pk)
