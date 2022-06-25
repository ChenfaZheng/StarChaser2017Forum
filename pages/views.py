from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


# class CoverPageView(TemplateView):
#     template_name = 'cover.html'


class SchedulePageView(TemplateView):
    template_name = 'schedule.html'