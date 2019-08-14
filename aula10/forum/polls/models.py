from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Question(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
