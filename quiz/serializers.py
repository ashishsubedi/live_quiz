from django.urls import reverse
from rest_framework import serializers
from .models import (Quiz,Problem,Option)
from random import sample



class QuizListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = '__all__'
    
        
    def get_url(self,obj):
        return reverse('quiz_detail',args=[obj.id])


class OptionRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        exclude = ['problem']
        depth = 0

class UserOptionRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        exclude = ['is_answer','problem']
        depth = 0





class ProblemRetrieveSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Problem
        
        exclude=['quiz']
        depth = 1

    def get_options(self,obj):
        query = Option.objects.filter(problem=obj)
        request = self.context.get('request', None)
        user = None
        if request:
            user = request.user
        print(user,request)
        if user and (user.is_superuser or obj.quiz.author == user):
            serializer = OptionRetrieveSerializer(query, many=True)
        else:
            serializer = UserOptionRetrieveSerializer(query, many=True)
        return serializer.data


class QuizRetrieveSerializer(serializers.ModelSerializer):
    # problems = ProblemRetrieveSerializer(many=True)
    problems = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()
 

    def get_problems(self, obj):
        
        request = self.context.get('request', None)
        ctx = {'request':request}
        user = None
        if request:
            user = request.user
        if obj.status == 1 or obj.status == 2:
            if user and (user.is_superuser or obj.author == user):
                pass
            else:
                return ProblemRetrieveSerializer(Problem.objects.none(), many=True,context=ctx).data

        query = Problem.objects.filter(quiz=obj)
        if len(query) > obj.total_questions_num:
            query = sample(list(query),obj.total_questions_num)
        serializer = ProblemRetrieveSerializer(query, many=True,context=ctx)
        return serializer.data
    def get_author(self,obj):
        return obj.author.username


    def get_status_name(self,obj):
        return obj.get_status_display()



    class Meta:
        model = Quiz
        fields = '__all__'
        