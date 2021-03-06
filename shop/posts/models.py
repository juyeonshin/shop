from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title =models.CharField(max_length=50, null=False)
    content =models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    view_count =models. IntegerField(default=0)
    created_at =models. DateTimeField(auto_now_add=True)
    upadated_at =models. DateTimeField(auto_now=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name="like_user_set", through="Like")

    @property
    def like_count(self):
        return self.like_user_set.count()
    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE) 

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user','post'))