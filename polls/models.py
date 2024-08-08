from django.db import models

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션 이라는걸 만든다.
# 이 모델에 맞는 테이블을 만든다.
# 질문: 여름에 놀러간다면 어디에 갈까?
# 산
# 강
# 바다
# 도심 호캉스

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_something = models.BooleanField(default=False)
    average_score = models.FloatField(default=0.0)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)