from django.db import models
from django.urls import reverse


ATTENDANCE_CHOICES = [
    ("毎回", ("毎回")),
    ("不定期", ("不定期")),
    ("初回のみ", ("初回のみ")),
    ("無し", ("無し")),
]

SATISFACTION_CHOICES = [
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
]

HARD_CHOICES = [
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
]

COLLEGE_CHOICES = [
    ("国際教養大学", ("国際教養大学")),
]


class Professor(models.Model):
    college = models.CharField(max_length=50, choices=COLLEGE_CHOICES)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    name = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='evaluation_names', null=True)
    comment = models.TextField(max_length=1000)
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES)
    hard = models.IntegerField(choices=HARD_CHOICES)

    evaluator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='evaluation_professors',
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
