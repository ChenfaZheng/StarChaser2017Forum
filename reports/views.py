from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin, 
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Report


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    context_object_name = 'report_list'
    template_name = 'reports/report_list.html'
    login_url = 'account_login'


class ReportCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Report
    fields = [
        'title',
        'abstract',
        'reporter',
        'note',
    ]
    template_name = 'reports/report_create.html'
    login_url = 'account_login'
    permission_required = 'reports.is_starchaser2017'
    
    # redirect to the detail view of the newly created report
    def get_success_url(self):
        return reverse_lazy('report_detail', args=[self.object.id])


class ReportDetailView(
        LoginRequiredMixin, 
        PermissionRequiredMixin, 
        DetailView, 
    ):
    model = Report
    context_object_name = 'report'
    template_name = 'reports/report_detail.html'
    login_url = 'account_login'
    permission_required = 'reports.is_starchaser2017'


# class ReportUpdateView(
#         LoginRequiredMixin,
#         PermissionRequiredMixin,
#         UpdateView,
#     ):
#     model = Report
#     fields = [
#         'title',
#         'abstract',
#         'reporter',
#         'note',
#     ]
#     template_name = 'reports/report_update.html'
#     login_url = 'account_login'
#     permission_required = 'reports.is_starchaser2017'


# class ReportDeleteView(
#         LoginRequiredMixin,
#         PermissionRequiredMixin,
#         DeleteView,
#     ):
#     model = Report
#     template_name = 'reports/report_delete.html'
#     login_url = 'account_login'
#     permission_required = 'reports.is_starchaser2017'
#     success_url = reverse_lazy('report_list')


class SearchResultsListView(ListView):
    model = Report
    context_object_name = 'report_list'
    template_name: str = 'reports/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Report.objects.filter(
            Q(title__icontains=query) | 
            Q(reporter__icontains=query) |
            Q(abstract__icontains=query) | 
            Q(note__icontains=query)
        )
