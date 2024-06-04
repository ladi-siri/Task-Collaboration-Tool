from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)