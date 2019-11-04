from django.db import models


class Trash(models.Model):

    # Image content
    content = models.TextField()

    # Inquiry timestamp
    timeStamp = models.DateTimeField(auto_now=True)

    # Inquiry result :
    # 0 represents cup
    # 1 represents book
    # 2 represents plastic wrapper
    # 3 represents bottle
    # 4 represents paper
    # 5 represents trash
    result = models.CharField(max_length=20)

