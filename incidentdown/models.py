from django.db import models

# Create your models here.


class IncidentDown(models.Model):
    caller_id = models.CharField(max_length=200)
    emailAdress = models.EmailField(max_length=200, blank=True, null="True")
    description = models.TextField()
    comments = models.TextField(blank=True, null="True")
    impact = models.IntegerField(default=4)
    urgency = models.IntegerField(default=4)
    worknotes = models.TextField(blank=True, null="True")
    assignment_group = models.CharField(max_length=200, blank=True, null="True")
    state = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    is_process = models.BooleanField(default=False)

    class Meta:
        db_table = 'SnowIncidentForm'
        ordering = ['-date']

    def __str__(self):
        return self.caller_id
    

