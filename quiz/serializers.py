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
        fields = '__all__'
        depth = 1


class ProblemRetrieveSerializer(serializers.ModelSerializer):
    options = OptionRetrieveSerializer(many=True)
    class Meta:
        model = Problem
        
        exclude=['quiz']
        depth = 1


class QuizRetrieveSerializer(serializers.ModelSerializer):
    # problems = ProblemRetrieveSerializer(many=True)
    problems = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()

    def get_problems(self, obj):
        query = Problem.objects.filter(quiz=obj)
        if len(query) > obj.total_questions_num:
            query = sample(list(query),obj.total_questions_num)
        serializer = ProblemRetrieveSerializer(query, many=True)
        return serializer.data
    def get_author(self,obj):
        return obj.author.username


    def get_status_name(self,obj):
        return obj.get_status_display()

    class Meta:
        model = Quiz
        fields = '__all__'
        