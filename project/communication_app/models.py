from django.db import models

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sent_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='received_messages')