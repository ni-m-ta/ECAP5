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


class Article(models.Model):
    college = models.CharField(max_length=50, choices=COLLEGE_CHOICES)
    professor_first = models.CharField(max_length=50)
    professor_last = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES)
    hard = models.IntegerField(choices=HARD_CHOICES)

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='author_professors',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('professors:detail', kwargs={'pk': self.pk})
