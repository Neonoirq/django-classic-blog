from django.db import models
from django.shortcuts import reverse




class Post(models.Model):
    title = models.CharField('Title', max_length=255, db_index=True)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    body = models.TextField('Post body', blank=True, db_index=True)
    author = models.CharField('Author', max_length=255, db_index=True)
    image = models.ImageField('Picture for post', upload_to='static/images/')
    date_pub = models.DateTimeField('Publication date', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    author = models.CharField('Comment author', max_length=255)
    email = models.EmailField('email', max_length=255)
    body = models.TextField('Comment body', max_length=2000, blank=False, db_index=True)
    date_pub = models.DateTimeField('Publication date', auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.author}'
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


