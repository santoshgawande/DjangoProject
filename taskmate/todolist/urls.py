from django.urls import path

urlpatterns = [
    path('task/', include("task.urls"))
]
