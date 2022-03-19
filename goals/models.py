from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    goal_name = models.CharField(max_length=100)
    goal_description = models.TextField()
    goal_completed = models.BooleanField(default=False)
    goal_set_date = models.DateField(auto_now_add=True)
    goal_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.goal_name