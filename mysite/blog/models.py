from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # Create models
    #'auth.User' refers to builtin admin users
    author = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL)#,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    # Set published_date when post is published
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Set comment to be approved
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # Send user to specefic page after create this model
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk}) # pk means primary key

    # Show if print this model
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # Set approved_comment True
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    # Show if print this model
    def __str__(self):
        return self.text
