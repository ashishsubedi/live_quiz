from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify 

User = get_user_model()


class Quiz(models.Model):
    author = models.ForeignKey(User,related_name='quiz',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255,default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True,null=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.created)
        super(Quiz, self).save(*args, **kwargs)


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
    quiz = models.ForeignKey(Quiz,related_name='scoreboard',on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,related_name='scoreboard',on_delete=models.DO_NOTHING)
    score =  models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name}->{self.score} on {self.quiz.title}"