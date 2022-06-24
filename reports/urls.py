from django.urls import path
from .views import (
    ReportListView, 
    ReportDetailView, 
    SearchResultsListView, 
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
)


urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'), 
    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('<uuid:pk>/', ReportDetailView.as_view(), name='report_detail'), 
    path('<uuid:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('<uuid:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('search/', SearchResultsListView.as_view(), name='search_results'), 
]