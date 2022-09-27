from pydoc import describe
from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    quiz_attempted = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    quiz_titles = models.TextField(default="")

    def __str__(self):
        return self.username

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    correct_ans = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.title) + "pk: " + str(self.pk)

class Quiz(models.Model):
    quiz_title = models.CharField(max_length=100)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_start = models.DateField()
    quiz_end = models.DateField()

    def __str__(self):
        # return str(self.quiz_title) + "pk: " + str(self.pk)
        return str(self.quiz_title) + str(self.pk)

class UserSub(models.Model):
    player_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.player_id.username) + "Quiz_submitted: " + self.quiz_id.quiz_title + "pk : " + str(self.pk)
