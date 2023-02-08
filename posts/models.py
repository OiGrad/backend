from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import User


class Love(models.Model):
 
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
   


class Post(models.Model):
    user= models.ForeignKey(User,related_name='User_post',on_delete=models.CASCADE)

    body = models.TextField()

    likes = GenericRelation(Love)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str (self.user)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    body = models.TextField()

    likes = GenericRelation(Love)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str (self.post.pk)
class CommentReplay(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)

    replay=models.TextField()

    likes = GenericRelation(Love)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.comment.pk)

    

class Attachment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.pk)
