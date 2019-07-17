
from django.db import models

class ShowManager(models.Manager):

    def validate(request, postdata):
        errors = {}
        print (" validate ")
        print (postdata)
        if (not postdata['title'].isalpha() or len(postdata['title']) < 2):
            errors['title'] = "Error: Title should be at least 2 characters and cannot be empty"
        if (not postdata['network'].isalpha() or len(postdata['network']) < 3):
            errors['network'] = "Error: Network should be at least 3 characters and cannot be empty"
        if (not postdata['desc'].isalpha() or len(postdata['desc']) < 10):
            errors['desc'] = "Error: Description should be at least 10 characters and cannot be empty"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=60)
    network = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    releasedate = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __unicode__(self):
        return " id: " + str(self.id) + " title: " + self.title + " network: " + self.network + " network: " + self.network