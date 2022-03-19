from rest_framework import viewsets, permissions
from .serializers import GoalSerializer, UserSerializer
from .models import Goal
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Register User': '/api/register/',
        'Login User': '/api/login/',
        'List': '/api/goal-list/',
        'Create': '/api/goal-create/',
        'Update': '/api/goal-update/<str:pk>/',
        'Delete': '/api/goal-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        if user.password == request.POST.get('password'):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_goal(request):
    goal = GoalSerializer(data=request.data)

    if goal.is_valid():
        goal.save()
        return Response(goal.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def goal_list(request):
    if request.query_params:
        items = Goal.objects.filter(user=request.query_params['user'])
    else:
        items = Goal.objects.all()

    if items:
        data = GoalSerializer(items)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def goal_update(request, pk):
    item = Goal.objects.get(pk=pk)
    data = GoalSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def goal_delete(request, pk):
    item = Goal.objects.get(pk=pk)

    if item:
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)