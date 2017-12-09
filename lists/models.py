from django.db import models

class Item(models.Model):
    """List items db"""
    text = models.TextField(default = "")
