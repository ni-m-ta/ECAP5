from django.db import models
from django.urls import reverse


TEXTBOOK_CHOICES = [
    (1, ("必須")),
    (2, ("不要")),
]

ATTENDANCE_CHOICES = [
    (1, ("毎回")),
    (2, ("不定期")),
    (3, ("初回のみ")),
    (4, ("無し")),
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


class Article(models.Model):
    course = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)
    professor = models.CharField(max_length=50)
    textbook = models.IntegerField(choices=TEXTBOOK_CHOICES, default=1)
    attendance = models.IntegerField(choices=ATTENDANCE_CHOICES, default=1)
    satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, default=1)
    hard = models.IntegerField(choices=HARD_CHOICES, default=1)

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='author_classes',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('classes:detail', kwargs={'pk': self.pk})
