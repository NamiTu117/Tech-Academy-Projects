from django.forms import ModelForm
from .models import Product

# __all__ selects all fields within Products
# and puts them the form
class ProductForm (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
