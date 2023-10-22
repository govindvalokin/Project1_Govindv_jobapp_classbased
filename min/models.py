from django.db import models

# Create your models here.
class Jobseeker(models.Model):
    first_name = models.CharField(max_length = 25, null = False)
    last_name = models.CharField(max_length = 25, null = True, blank = True)
    country_code = [
                    ('+91','+91'),
                    ('+1','+1')
                    ]
    code = models.CharField(max_length = 3, null = False, choices = country_code, default= '+91')
    phone = models.CharField(max_length = 25, null = False)
    email = models.EmailField(null = False)
    dob = models.DateField(null = False)
    genderchoice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    gender = models.CharField(null = False, max_length = 6, choices = genderchoice, default = None)
    jobchoice = [
        ("","Choose Job Role"),
        ('Developer','Developer'),
        ('Testing','Testing'),
        ('Devops','Devops'),
        ('Operations','Operations'),
        ('Accounting','Accounting')
    ]
    job_role = models.CharField(null = False, max_length = 10, choices = jobchoice)
    experiencelevel = [
        ("","Choose Experience (In years)"),
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5+','5+')

    ]
    experience = models.CharField(max_length = 2, null = False, choices = experiencelevel)
    address_line_one = models.CharField(null = True, max_length = 35, blank=True)
    address_line_two = models.CharField(null = True, max_length = 35, blank=True)
    city = models.CharField(null = True, max_length = 20, blank=True)
    state = models.CharField(null = True, max_length = 20, blank=True)
    zip_code = models.CharField(max_length = 6, null = True, blank=True)
    countrychoices = [
        ("","Choose Country"),
        ('India','India'),
        ('US','US')
    ]
    country = models.CharField(null=True, max_length=5, choices = countrychoices, blank=True)
    # status = models.CharField(null=False, default="test", max_length=10)

    def __str__(self):
        return self.first_name