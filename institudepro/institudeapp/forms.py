from django import forms
from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'EmailId'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('django', 'Django'),
        ('restapi', 'RestApi'),
        ('ui', 'UI')
    )

    course = MultiSelectFormField(max_length=100,choices=COURSES_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'HYDERABAD'),
        ('bang', 'BANGLORE'),
        ('ind', 'INDORE'),
    )

    location = MultiSelectFormField(max_length=100, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('morning', 'MORNING'),
        ('afternoon', 'AFTERNOON'),
        ('night', 'NIGHT'),
    )

    shift = MultiSelectFormField(max_length=100, choices=SHIFT_CHOICES)


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Rating'
            }
        )
    )

    feedback = forms.CharField(
        label='Enter Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Feedback'
            }
        )
    )