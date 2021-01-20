from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()


class Recruit(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
    is_available = models.BooleanField(default=False)


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="default@site.com")
    phone = models.CharField(max_length=30)
    applying_parts = models.ManyToManyField(Part)
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    max_score = models.IntegerField()


class Evaluation(models.Model):
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Application, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.applicant.name} by {self.evaluator.name}'
