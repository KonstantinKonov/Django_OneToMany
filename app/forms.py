from django.forms import ModelForm
from .models import Company, Products


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('id', )


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ('id', )
