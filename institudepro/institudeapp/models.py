from django.db import models
from  multiselectfield import MultiSelectField


class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    COURSES_CHOICES = (
        ('py','Python'),
        ('django','Django'),
        ('restapi','RestApi'),
        ('ui','UI')
    )

    courses = MultiSelectField(max_length=100,choices=COURSES_CHOICES)

    LOCATION_CHOICES = (
        ('hyd','HYDERABAD'),
        ('bang','BANGLORE'),
        ('ind','INDORE'),
    )

    location = MultiSelectField(max_length=100,choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('morning','MORNING'),
        ('afternoon','AFTERNOON'),
        ('night','NIGHT'),
    )

    shift = MultiSelectField(max_length=100,choices=SHIFT_CHOICES)


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField()
    feedback = models.CharField(max_length=200)