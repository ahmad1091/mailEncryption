from django.db import models

# Create your models here.

class Note(models.Model):
    note = models.TextField() # should stored hashed // required
    destructionOption = models.IntegerField() # 1 for After read, 2 for destruction date // required
    creationDate = models.DateTimeField() # should came from client side // optional
    destructionDate = models.DateTimeField() # should came from client side // optional
    password = models.CharField(max_length=50) # for opening the encrepted message // optional
    notificationEmail = models.EmailField() # to notify the sender that note have been read // optional
    sendEmail = models.BooleanField(default=False) # if true send E-mail notify the sender that note have been read // optional
    isDestroyed = models.BooleanField(default=False) # if true return message for the client side informs that the message is destroyed // optional
    confirmation = models.BooleanField(default=False) # if true send True filed fro the client side  // optional

