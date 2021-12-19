from django.db import models
# Create your models here.


class blogpost(models.Model):
    post_id = models.IntegerField()
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title
