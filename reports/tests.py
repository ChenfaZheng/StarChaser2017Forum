from urllib import response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from .models import Report


class ReportTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser', 
            email='reviewuser@email.com', 
            password='testreviewpass'
        )

        self.special_permission = Permission.objects.get(
            codename='special_status', 
        )

        self.report = Report.objects.create(
            title = 'Test Report', 
            reporter = 'AB Chen', 
            abstract = 'something useless', 
            note = 'nothing', 
        )

        # self.review = Review.objects.create(
        #     report = self.report, 
        #     author = self.user, 
        #     review = 'Test Review', 
        # )

    def test_report_listing(self):
        self.assertEqual(f'{self.report.title}', 'Test Report')
        self.assertEqual(f'{self.report.reporter}', 'AB Chen')
        self.assertEqual(f'{self.report.abstract}', 'something useless')
        self.assertEqual(f'{self.report.note}', 'nothing')
    
    # def test_report_list_view_for_logged_in_user(self):
    #     self.client.login(email='reviewuser@email.com', password='testreviewpass')
    #     response = self.client.get(reverse('report_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Test Report')
    #     self.assertTemplateUsed(response, 'reports/report_list.html')
    
    # def test_report_list_view_for_logged_out_user(self):
    #     self.client.logout()
    #     response = self.client.get(reverse('report_list'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '%s?next=/reports/'%(reverse('account_login')))
    #     response_redirects = self.client.get('%s?next=/reports/'%(reverse('account_login')))
    #     self.assertContains(response_redirects, 'Log In')

    # def test_report_detail_view_with_permissions(self):
    #     self.client.login(email='reviewuser@email.com', password='testreviewpass')
    #     self.user.user_permissions.add(self.special_permission)
    #     response = self.client.get(self.report.get_absolute_url())
    #     no_response = self.client.get('/reports/12345/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, 'Test Report')
    #     self.assertContains(response, 'Test Review')
    #     self.assertTemplateUsed(response, 'reports/report_detail.html')
