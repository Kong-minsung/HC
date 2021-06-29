from django.db import models

# Create your models here.
class Hc(models.Model):

    like_choices = {
        ('music','Music'),
        ('movie','Movie'),
        ('animal','Animal'),
        ('sport','Sport'),
    }
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pub_date = models.DateTimeField()
    email = models.EmailField(max_length=100)
    introduce = models.TextField()
    like = models.CharField(max_length=80, choices=like_choices, null=True)
    image = models.ImageField(upload_to = "Hc/", blank =True, null=True)
    

    def __str__(self):
        return self.name

    def info_summary(self):
        return self.introduce[:100]