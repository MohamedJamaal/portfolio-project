from django.db import models

# Create your models here.

# Create blog model
#title
#pub-date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')



    def __str__(self):
            return self.title
# add the blog app to the settings


# create migrations
# migrate


# add to admin
