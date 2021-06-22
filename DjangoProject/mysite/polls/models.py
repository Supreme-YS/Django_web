from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # DB에 있는 객체를 터미널 상에 표현하기 위한 메서드
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # DB에 있는 객체를 터미널 상에 표현하기 위한 메서드
    def __str__(self):
        return self.choice_text