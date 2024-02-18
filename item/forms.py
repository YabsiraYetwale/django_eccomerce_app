from .models import ItemModel
from django import forms
INPUT_CLASSES = 'w-[100%] py-[10px] px-12 rounded-xl border '

class ItemForm(forms.ModelForm):
    class Meta:
        model=ItemModel
        fields=('catagory','name','description','price','image','isSold')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES ,
                'placeholder':'write name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-[100%] py-4 px-12 rounded-xl border h-[200px]',
                'placeholder':'write description'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder':'write the price'
            }),
            
        }