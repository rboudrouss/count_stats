from django.db import models

# Create your models here.


class UserData(models.Model):
    user_id = models.CharField(max_length=20)
    avatar_url = models.CharField(max_length=200, default="nan")
    name = models.CharField(max_length=50, default="nan")
    discriminator = models.CharField(max_length=5, default="nan")
    ghost = models.BooleanField(default=True)
    nb_msg = models.IntegerField(default=0)
    top = models.IntegerField(default=0)

    def __repr__(self):
        return f"<User {self.name}#{self.discriminator}>"


class MessageData(models.Model):
    message_id = models.CharField(max_length=20)
    author_id = models.CharField(max_length=20, default="0")
    content = models.CharField(max_length=2000, default="nan")
    date = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Message id={self.message_id} date={self.date}>"
