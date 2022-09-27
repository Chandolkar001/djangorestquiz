from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
import json

from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, status 

# Create your views here.

class UserViewSet(viewsets.ViewSet):

    # List All Users -- get method
    def list(self, request):
        users = Profile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # Retrieve Particular User -- get method
    def retrieve(self, request, pk = None): 
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # Create a new User -- post method
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# complete account details
class AccountDetailView(APIView):
    serializer = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        data = {}
        id = request.user.id
        user = Profile.objects.filter(id=id).first()
        data['username'] = user.username
        data['quizzes_attempted'] = user.quiz_attempted
        data['quiz_titles'] = user.quiz_titles
        return Response(data, status=201)

# question creator : only admin accessible
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

# quiz creator : only admin accessible
class QuizCreater(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminUser]

# Particular quiz details with pk
class QuizList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

# Submission process and evaluation with score
class ResponseSub(APIView):
    queryset = UserSub.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RespondSerializer
    

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            # extract answer from user 
            answer = request.data["answer"]
            quiz_id = request.data["quiz_id"]
            answer  = answer.split(" ")
            answer = [each_string.lower() for each_string in answer]
            separator = ""
            answer = separator.join(answer)

            profile = Profile.objects.get(id = request.user.id)
            print(profile)

            submission = Quiz.objects.filter(id = quiz_id)
            ques_id = str(submission[0])

            # extract correct ans from question model based on ID
            correct_ans = Question.objects.get(id = ques_id[-1]).correct_ans
            correct_ans = correct_ans.split(" ")
            correct_ans = [each_string.lower() for each_string in correct_ans]
            separator = ""
            correct_ans = separator.join(correct_ans)

            quiz_attended = profile.quiz_titles.split(" ")

            # compare the answers and display the score
            if answer == correct_ans:
                profile.score += 1
                profile.quiz_attempted += 1           
                quiz_attended.append(quiz_id)
                profile.quiz_titles = " ".join(map(str, quiz_attended))
                data = {}
                data['username'] = profile.username
                data['score'] = profile.score 

            profile.save(update_fields = ["score", "quiz_attempted", "quiz_titles"])

            return Response(data, status=201)



