from django.db import models




class Post(models.Model):
    title = models.CharField('Title', max_length=255, db_index=True)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    body = models.TextField('Post body', blank=True, db_index=True)
    author = models.CharField('Author', max_length=255)
    image = models.ImageField('Picture for post', upload_to='images/')
    date_pub = models.DateTimeField('Publication date', auto_now_add=True)
    

    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

