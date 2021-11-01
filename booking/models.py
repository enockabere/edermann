from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField

# Create your models here.
class Estate(models.Model):
    name = models.CharField( verbose_name="Estate Name" ,max_length=200, unique=True)
    logo = CloudinaryField('image')
    about = TextField(verbose_name="About Estate")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)