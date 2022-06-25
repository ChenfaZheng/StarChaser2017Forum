from django.urls import path
from .views import HomePageView, AboutPageView, SchedulePageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('schedule/', SchedulePageView.as_view(), name='schedule'),
    # path('cover/', CoverPageView.as_view(), name='cover'),
    path('', HomePageView.as_view(), name='home'),
]
