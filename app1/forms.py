from django import forms
from .models import Customer, Product

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'customer_id', 'email', 'phone_number', 'city', 'street', 'postal_code', 'fax']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'street', 'city', 'postal_code', 'phone_number', 'fax', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['part_code', 'part_name', 'details', 'material_used']
        widgets = {
            'part_code': forms.TextInput(attrs={'class': 'form-control'}),
            'part_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'material_used': forms.TextInput(attrs={'class': 'form-control'}),
        }