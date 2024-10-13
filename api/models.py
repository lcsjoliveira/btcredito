from django.db import models


class CNJRequest(models.Model):
    cnj_number = models.CharField(max_length=25, unique=True)
    external_service_response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cnj_number
