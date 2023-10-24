from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Jobseeker
from .forms import JobForm
from django.db.models import Q

# from datetime import date
# import re
# import datetime
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.


# View for getting all user data
class UserListView(ListView):
    model = Jobseeker
    template_name = "django_listing_page.html"
    context_object_name = "data"

    # Altering inbuilt function to display data in LIFO order
    def get_queryset(self):
        return Jobseeker.objects.all().order_by("-id")

#view for showing particular user as per the  search request
class SearchList(ListView):
    model = Jobseeker
    template_name = "django_listing_page.html"
    context_object_name = "data"

    def get_queryset(self):
        search = self.request.GET.get("search_bar")
        if search:
            return Jobseeker.objects.all().filter(Q(first_name = search) | Q(email = search))


# View for creating new user
class UserCreateView(CreateView):
    model = Jobseeker
    template_name = "form.html"
    form_class = JobForm
    success_url = reverse_lazy("user_data")

    # Function to display success message
    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        form.instance.first_name = first_name.capitalize()
        form.save()
        messages.add_message(
            self.request, messages.INFO, "Successfully Submitted your Application"
        )
        return super().form_valid(form)
    #function to display error message 
    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO, form.errors)
        return redirect("new_user")

# view for updating existing user data
class UserUpdateView(UpdateView):
    model = Jobseeker
    template_name = "django_update_page.html"
    form_class = JobForm
    success_url = reverse_lazy("user_data")

    # Function to display success message
    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        form.instance.first_name = first_name.capitalize()
        form.save()
        messages.add_message(
            self.request, messages.INFO, "Successfully Updated your Data"
        )
        return super().form_valid(form)


# View for deleting existing user
class UserDeleteView(DeleteView):
    model = Jobseeker
    success_url = reverse_lazy("user_data")
