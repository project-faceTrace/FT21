from django.db import models
class Image(models.Model):
    name=models.CharField(max_length=64)
    image=models.ImageField(upload_to='Training_images/')
class Admin(models.Model):
    admin_id=models.CharField(max_length=16)
    admin_name=models.CharField(max_length=30)
    admin_email=models.EmailField()
    admin_contact=models.CharField(max_length=10)
    def __str__(self):
        return "%s" %self.admin_id
    class Meta:
        db_table='admin'
# Create your models here.
