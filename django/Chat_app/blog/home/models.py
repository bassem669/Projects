from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    message = models.TextField(max_length=300)
    date_published = models.DateTimeField(auto_now_add=True)

class Commentre(Message):
    message_ref = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='commentaires', null=True, blank=True)
