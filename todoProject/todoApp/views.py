from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks, Category
from .forms import TaskForm
from .serializers import TaskSerializer, RegisterSerializer, CategorySerializer
from rest_framework import viewsets, generics, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import TaskPagination

# Create your views here.
# Applying CRUD rule (Create, Read, Update, Delete)

# Create/add a new task
def task_create_view(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form':form})

# Read/List all tasks
def task_read_view(request):
    tasks = Tasks.objects.all()
    return render(request, 'list.html', {'tasks':tasks})

# Update/Edit a task
def task_update_view(request, task_id):
    task = get_object_or_404(Tasks, id=task_id) # get_object_or_404 fetches an object from the database and if it doesn't exist, automatically show a 404 error page .It helps to handle the error without crashing the app
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update.html', {'form':form})

# Delete a task
def task_delete_view(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete.html', {'task':task})

# Delete all tasks
def task_delete_all_view(request):
    if request.method == "POST":
        Tasks.objects.all().delete()
        return redirect('task_list')
    return render(request, 'delete_all.html')

class TaskViewset(viewsets.ModelViewSet):
    # queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    pagination_class = TaskPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed', 'category'] # filter by completed status and category
    search_fields = ['title', 'category__name'] # search by title and category name (category__name is for searching by category name instead of id)
    
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # permission_classes helps to prevent anonymous users from accessing tasks
    # get_queryset... each user only sees their own tasks
    # perform_create... when task is created, django automatically attaches logged-in user. You no longer manually assign users

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({
                "message": "Login successful",
                "user": user.username
            })
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
