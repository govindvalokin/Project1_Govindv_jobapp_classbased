from django import forms
from .models import Jobseeker


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = '__all__'    
        labels = {
            'first_name':'First Name',
             'last_name':'Last Name',
             'code':'Country Code',
             'phone':'Phone',
             'email':'Email',
             'dob':'DOB',
             'gender':'Gender',
             'job_role':'Job Role',
             'Experience':'Experience',
             'address_line_one':'Address Line 1',
             'address_line_two':'Address Line 2',
             'city':'City',
             'state':'State',
             'zip_code':'Zip Code',
             'country':'Country'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'id': "firstName", 
                'placeholder': "Type your First Name",
                'required': "False",
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': "Type your First Name",
                
            }),
            'code': forms.Select(attrs={
                'id': "code",
                'choices': ["country_code"],
                'initial': "+91",
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "Type your Phone Number",
                'id': "mob",
                'class': "phoneno",  
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "Type your Email",
                'id': "email"
            }),
            'dob': forms.widgets.DateInput(attrs={
                'placeholder': "Type your Date of Birth",
                'type': "date",
                'id': "date",
            }),
            'gender': forms.RadioSelect(attrs={
                'name': "gender",
                
            }),
            'job_role': forms.Select(attrs={
                'id': "role",
                'class': "job-role"
            }),
            'experience': forms.Select(attrs={
                'id': "experience",
                'class': "job-experience"
            }),
            'country': forms.Select(attrs={
                'id': "country",
                'class': "country",
            }),
            'address_line_one': forms.TextInput(attrs={
                'id': "address1", 
                'placeholder': "Type your Address",
            }),
            'address_line_two': forms.TextInput(attrs={
                'id': "address1",
                'placeholder': "Type your Address",
            }),
            'city': forms.TextInput(attrs={
                'id': "city", 
                'placeholder':"Type your City",
            }),
            'state': forms.TextInput(attrs={
                'id': "state", 
                'placeholder': "Type your State",
            }),
            'zip_code': forms.TextInput(attrs={
                'id': "zipCode", 
                'placeholder': "Type your Zip Code",
                
            }),
            

        }


















# class jobform(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=25)
#     last_name = forms.CharField(label="Last Name",max_length=25)
#     code_choice = [
#         ("india",'+91'),
#         ("US",'+1')
#     ]
#     code = forms.ChoiceField(choices = code_choice)
#     phone = forms.IntegerField(label="phone", max_value=10, widget=forms.TextInput(attrs={'placeholder':'phone'})required=True)
#     email = forms.EmailField(null=False)
    
#     dob = forms.DateField(null=False)
#     genderchoice= [
#         ('male','male'),
#         ('female','female'),
#         ('other','other')
#     ]
#     gender = forms.CharField(null=False, max_length=6, choices = genderchoice)
#     jobchoice = [
#         ('developer','developer'),
#         ('testing','testing'),
#         ('devops','devops')
#     ]
#     job_role = forms.CharField(null=False, max_length=10, choices= jobchoice)
#     experiencelevel = [
#         ('0','0'),
#         ('1','1'),
#         ('2','2'),
#         ('3','3'),
#         ('4','4'),
#         ('5+','5+')
#     ]
#     experience = forms.IntegerField(null=False, choices=experiencelevel)
#     address = forms.CharField(null=False, max_length=35)
#     city = forms.CharField(null=False, max_length=20)
#     state = forms.CharField(null=False, max_length=20)
#     zip_code = forms.IntegerField(null=False)
#     countrychoices = [
#         ('india','india'),
#         ('caneda','caneda'),
#         ('uk','uk'),
#         ('us','us')
#     ]
#     country = forms.CharField(null=False, max_length=20, choices=countrychoices)