from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
            "AccountCreate": False,
            "account_form": AccountForm(),
            "add_account_form": AddAccountForm(),
        }

    # To do get
    def get(self, request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request, "register.html", context=self.params)

    # To do post
    def post(self, request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # To check how well the form works
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # To save account info
            account = self.params["account_form"].save()
            # To make password hash
            account.set_password(account.password)
            # To update hashed password
            account.save()

            # Additional info
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1
            add_account.user = account

            # To save accounts
            add_account.save()

            # To update account info
            self.params["AccountCreate"] = True

        else:
            # If the form is not good
            print(self.params["account_form"].errors)

        return render(request, "register.html", context=self.params)
