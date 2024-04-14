from django.contrib import admin
from django.urls import path

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchilarView.as_view()),
    path('qoshiqchilar/<int:pk>/', QoshiqchiAPIView.as_view()),
    path('qoshiqlar/', QoshiqlarAPIView.as_view()),

]
