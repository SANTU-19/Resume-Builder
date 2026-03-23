from django.db import models

# Create your models here.
class Resume(models.Model):
    level_choice=[
                ('entry','Entry level'),
                ( 'mid','Mid level'),
                ('expert','Experienced'),
                ]
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
    choice=models.CharField(max_length=10,choices=level_choice)
    answer=models.JSONField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name