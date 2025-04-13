from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
