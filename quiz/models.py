from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class Quiz(models.Model):
    STATUS_TYPE    = (
        (1, 'Draft'),
        (2, 'Private'),
        (3, 'Public'),
    )
    author = models.ForeignKey(User,related_name='quiz',on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_TYPE)
    title = models.CharField(max_length=255,default='')
    timelimit = models.DurationField(default=timedelta(minutes=20))
    total_questions_num = models.IntegerField(default=10)
    available_attempts = models.IntegerField(default=3)
    schedule_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Quizzes'
    
    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super(Quiz, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('quiz_detail',args=[self.id])

class Problem(models.Model):
    question = models.TextField()
    point = models.IntegerField(default = 1)
    
    quiz = models.ForeignKey('Quiz',related_name='problems',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}"
    
    def check_answer_exists(self,option):
        return self.options.filter(id=option.id,is_answer=True).exists()

class Option(models.Model):


    option = models.CharField(max_length=255)
    is_answer = models.BooleanField()
    problem = models.ForeignKey(Problem,related_name='options',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.option} for {self.problem.question}"

class ScoreBoard(models.Model):
    quiz = models.ForeignKey(Quiz,related_name='scoreboard',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='scoreboard',on_delete=models.CASCADE)
    score =  models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name}->{self.score} on {self.quiz.title}"

    class Meta:
        verbose_name_plural = 'Score Board'