from django.db import models
from django.urls import reverse
from core.shared import Postable, TimeStampedModel
from .post import Post
from account.models import Account 

## NEEDS WORK 
class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    commentor = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"pk": self.pk})
    