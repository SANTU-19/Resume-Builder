from django.urls import path
from .views import create_resume,save_answers,get_resume
urlpatterns = [
    path('resume/',create_resume),
    path('resume/<int:id>/',get_resume),
    path('resume/<int:id>/answers/',save_answers)

]
