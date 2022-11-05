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
    college = models.CharField(max_length=50, choices=COLLEGE_CHOICES, verbose_name='大学名(例: 国際教養大学)')
    name = models.CharField(max_length=50, verbose_name='英字で教授名を入力(例:Taro Sato or Eric Raymond)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['college', 'name']


class Evaluation(models.Model):
    name = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='evaluation_names', null=True, verbose_name='教授名')
    comment = models.TextField(max_length=1000, verbose_name='評価コメント')
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='出席')
    satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, verbose_name='満足度')
    hard = models.IntegerField(choices=HARD_CHOICES, verbose_name='厳しさ度')

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
