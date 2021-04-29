from django.db import models

# Create your models here.
class Pribadi(models.Model):
    nama = models.CharField(max_length=255, blank=False, null=False)
    alamat = models.TextField()
    ttl = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama
    
    
class Project(models.Model):
    status1= (
        ('done','done'),
        ('draft','draft') 
    )
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='img')    
    status = models.CharField(max_length=255, blank=False, choices=status1)
    timtestamp = models.DateTimeField(auto_now_add=True, blank=False,null=False)
    
    def __str__(self):
        return self.title