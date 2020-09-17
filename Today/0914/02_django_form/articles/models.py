from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(300, 200)],
        format='JPEG',
        options={'quality': 60},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
