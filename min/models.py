from django.db import models
from django.core.exceptions import ValidationError
import re
from datetime import date, datetime


# Create your models here.
class Jobseeker(models.Model):
    # First name custom validation
    def validate_first_name(first_name):
        if (
            (first_name == None)
            or (first_name == "")
            or (len(first_name) < 3)
            or (len(first_name) > 25)
        ):
            raise ValidationError(f"{first_name} is invalid")

    # Phone number custom validation
    def validate_phone(phone):
        regexmob = r"^\d{10}$"
        matchvalue = re.match(regexmob, phone)
        if phone == "" or matchvalue == None:
            raise ValidationError(f"{phone} is invalid")

    # Custom date validation
    # def validate_date(dob):
    #     today = date.today()
    #     givenDate = datetime.strptime(str(dob), "%Y-%m-%d").date() #converting string to date object
    #     if ((today - givenDate).total_seconds() / 31536000 < 18):
    #         raise ValidationError(f"{dob} is invalid")

    def validate_date(dob):
        today = date.today()
        if (today - dob).total_seconds() / 31536000 < 18:
            raise ValidationError(f"{dob} is invalid")

    first_name = models.CharField(
        max_length=25, null=False, validators=[validate_first_name]
    )
    last_name = models.CharField(max_length=25, null=True, blank=True)
    country_code = [("+91", "+91"), ("+1", "+1")]
    code = models.CharField(
        max_length=3, null=False, choices=country_code, default="+91"
    )
    phone = models.CharField(max_length=10, null=False, validators=[validate_phone])
    email = models.EmailField(null=False, unique=True)
    dob = models.DateField(null=False, validators=[validate_date])
    genderchoice = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    gender = models.CharField(
        null=False, max_length=6, choices=genderchoice, default=None
    )
    jobchoice = [
        ("", "Choose Job Role"),
        ("Developer", "Developer"),
        ("Testing", "Testing"),
        ("Devops", "Devops"),
        ("Operations", "Operations"),
        ("Accounting", "Accounting"),
    ]
    job_role = models.CharField(null=False, max_length=10, choices=jobchoice)
    experiencelevel = [
        ("", "Choose Experience (In years)"),
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5+", "5+"),
    ]
    experience = models.CharField(max_length=2, null=False, choices=experiencelevel)
    address_line_one = models.CharField(null=True, max_length=35, blank=True)
    address_line_two = models.CharField(null=True, max_length=35, blank=True)
    city = models.CharField(null=True, max_length=20, blank=True)
    state = models.CharField(null=True, max_length=20, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)
    countrychoices = [("", "Choose Country"), ("India", "India"), ("US", "US")]
    country = models.CharField(
        null=True, max_length=5, choices=countrychoices, blank=True
    )
    # status = models.CharField(null=False, default="test", max_length=10)
    # user_id = models.CharField(max_length=10, null=False, unique=True)
    def __str__(self):
        return self.first_name
