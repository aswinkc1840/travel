from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    def __str__(self):
        return format(self.name)


class tourdate(models.Model):
    date=models.DateField()
    tittle=models.CharField(max_length=300)
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='picture')

    def __str__(self):
        return format(self.tittle)

