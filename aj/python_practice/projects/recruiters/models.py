from django.db import models

# Create your models here.

from django.conf import settings

User = settings.AUTH_USER_MODEL

class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='recruiters')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email} - {self.company.name}"