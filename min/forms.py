from django import forms
from .models import Jobseeker


# django model form for users
class JobForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "code": "Country Code",
            "phone": "Phone",
            "email": "Email",
            "dob": "DOB",
            "gender": "Gender",
            "job_role": "Job Role",
            "Experience": "Experience",
            "address_line_one": "Address Line 1",
            "address_line_two": "Address Line 2",
            "city": "City",
            "state": "State",
            "zip_code": "Zip Code",
            "country": "Country",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "id": "firstName",
                    "placeholder": "Type your First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Type your First Name",
                }
            ),
            "code": forms.Select(
                attrs={
                    "id": "code",
                    "choices": ["country_code"],
                    "initial": "+91",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Type your Phone Number",
                    "id": "mob",
                    "class": "phoneno",
                }
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Type your Email", "id": "email"}
            ),
            "dob": forms.widgets.DateInput(
                attrs={
                    "placeholder": "Type your Date of Birth",
                    "type": "date",
                    "id": "date",
                }
            ),
            "gender": forms.RadioSelect(
                attrs={
                    "name": "gender",
                }
            ),
            "job_role": forms.Select(attrs={"id": "role", "class": "job-role"}),
            "experience": forms.Select(
                attrs={"id": "experience", "class": "job-experience"}
            ),
            "country": forms.Select(
                attrs={
                    "id": "country",
                    "class": "country",
                }
            ),
            "address_line_one": forms.TextInput(
                attrs={
                    "id": "address1",
                    "placeholder": "Type your Address",
                }
            ),
            "address_line_two": forms.TextInput(
                attrs={
                    "id": "address1",
                    "placeholder": "Type your Address",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "id": "city",
                    "placeholder": "Type your City",
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "id": "state",
                    "placeholder": "Type your State",
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "id": "zipCode",
                    "placeholder": "Type your Zip Code",
                }
            ),
        }
