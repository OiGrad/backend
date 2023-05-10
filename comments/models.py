from django.db import models

from users.models import User


class Comment(models.Model):
    text = models.TextField()
    parent_type = models.CharField(max_length=10,
                                   choices=[('post', 'Post'), ('place', 'Place'), ('comment', 'Comment')])
    parent_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
