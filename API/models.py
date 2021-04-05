from django.db import models

# Create your models here.
class UserData(models.Model):
    avatar_url  = models.CharField(max_length=100)
    name        = models.CharField(max_length=50)
    discriminator = models.CharField(max_length=5)
    user_id = models.CharField(max_length=20)

    def __repr__(self):
        return f"<User {self.name}#{self.discriminator}>"

class MessageData(models.Model):
    message_id  = models.CharField(max_length=20)
    author_id   = models.CharField(max_length=20)
    content     = models.CharField(max_length=2000)
    date        = models.DateTimeField()

    def __repr__(self):
        return f"<Message id={self.id} date={date}>"
