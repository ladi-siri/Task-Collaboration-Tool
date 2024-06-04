from django.urls import path, include

urlpatterns = [
    path('tasks/', include('task_app.urls')),
    path('files/', include('file_app.urls')),
    path('messages/', include('communication_app.urls')),
]