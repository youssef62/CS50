from auctions.models import * 
from django import forms


class ListingForm(forms.ModelForm) : 

    class Meta : 
        model = Listing 
        fields = ['title','description','photo','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
           }),
            'description' : forms.TextInput(attrs={'class':'form-control'} ),
            'photo': forms.TextInput(attrs={'class': 'form-control' ,
            'placeholder': 'image url '})
        }
    min_bid = forms.FloatField(required=False,widget = forms.TextInput(attrs={'class': 'form-control'}))


