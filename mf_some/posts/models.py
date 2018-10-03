from django.db import models


class Post(models.Model):
    author = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author} @ {self.created_at}'


class Like(models.Model):
    post = models.ForeignKey('posts.Post', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -> {self.post}'
