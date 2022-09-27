from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserViewSet.as_view(actions={'get': 'list', 'post': 'create'}), name = 'list-create-users'),
    path('users/<int:pk>', UserViewSet.as_view(actions={'get': 'retrieve'}), name = 'retrieve-user'),
    path('create_question/', QuestionList.as_view()),
    path('create_quiz/', QuizCreater.as_view()),
    path('quiz/<int:pk>', QuizList.as_view()),
    path('submit_quiz/', ResponseSub.as_view()),
    path('account_detail/', AccountDetailView.as_view()),
]