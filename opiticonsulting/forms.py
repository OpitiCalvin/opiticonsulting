from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'full-name',
                'placeholder':"Full Names",
                'name':"full-name",
                'class':"input100"
                }),
        label='',
        max_length=50)
    
    phone = forms.CharField(
        required = False,
        max_length=15,
        widget=forms.TextInput(
            attrs={
<<<<<<< HEAD
                'placeholder':"Eg. +1 800 000000",
=======
                'placeholder':"+27 012 345 6789",
>>>>>>> 5bda11ab405cc51c556a82fdd92953ddce5676eb
                'name':"phone",
                'class':"input100"
                }),
        label=''
        )
    email = forms.EmailField(
        max_length=25,
        widget=forms.EmailInput(
            attrs={
<<<<<<< HEAD
                'placeholder':"Eg. example@email.com",
=======
                'placeholder':"example@email.com",
>>>>>>> 5bda11ab405cc51c556a82fdd92953ddce5676eb
                'name':"email",
                'class':"input100"
                }),
        label=''
        )
    city = forms.CharField(
        required = False,
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'placeholder':"City/Town",
                'name':"city-name",
                'class':"input100"
                }),
        label=''
        )
    country = forms.CharField(
        required = False,
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Country",
                'name':"country-name",
                'class':"input100"
                }),
        label=''
        )
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Subject",
                'name':"subject",
                'class':"input100"
                }),
        label=''
        )
    message = forms.CharField(
        max_length=200,
        widget = forms.Textarea(
            attrs={
                'placeholder':'Write us a message',
                'name':'message',
                'class':'input100'
                }),
        label=''
        )
    
