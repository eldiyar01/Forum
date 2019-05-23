import uuid
from django.db import models
from django.urls import reverse



def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext.lower())

    return 'media/{sub}/{filename}'.format(
        sub=filename[:2],
        filename=filename
)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class News(models.Model):
    author = models.ForeignKey(
        'user.User',
        on_delete=models.SET_NULL,
        null=True,
    )
    categories = models.ManyToManyField('Category', blank=True, related_name='news')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        ordering = ["add_time"]

    def get_absolute_url(self):
        return reverse('blog:news_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=False)

    class Meta:
        ordering = ["add_time"]

    def __str__(self):
        return self.content

