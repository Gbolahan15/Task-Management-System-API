from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = DefaultRouter()
router.register('tasks', views.TaskViewset, basename='tasks')
router.register('categories', views.CategoryViewset, basename='categories')

urlpatterns = [
    path('', views.task_read_view, name="task_list"),
    path('create/', views.task_create_view, name="task_create"),
    path('update/<int:task_id>/', views.task_update_view, name="task_update"),
    path('delete/<int:task_id>/', views.task_delete_view, name="task_delete"),
    path('delete-all/', views.task_delete_all_view, name="task_delete_all"),

    path('api/', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]