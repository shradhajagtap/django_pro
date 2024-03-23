from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "company_owner": forms.TextInput(attrs={"class": "form-control"}),
            "company_total_emp": forms.NumberInput(attrs={"class": "form-control"}),
            "company_city": forms.TextInput(attrs={"class": "form-control", "rows": 5}),
            "company_state": forms.TextInput(attrs={"class": "form-control", "rows": 5}),
            "city_pincode": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_mode": forms.Select(attrs={"class": "form-control"})
        }
