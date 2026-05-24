from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewset, basename='tasks')

urlpatterns = [
    path('', views.task_read_view, name="task_list"),
    path('create/', views.task_create_view, name="task_create"),
    path('update/<int:task_id>/', views.task_update_view, name="task_update"),
    path('delete/<int:task_id>/', views.task_delete_view, name="task_delete"),
    path('delete-all/', views.task_delete_all_view, name="task_delete_all"),

    path('api/', include(router.urls)),
]