from django.shortcuts import render
from .models import ContactData,FeedbackData
from .forms import FeedbackForm,ContactForm
from django.http.response import HttpResponse


def home_view(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.method)
        if form.is_valid:
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('mobile')
            course = form.cleaned_data.get('course')
            location = form.cleaned_data.get('location')
            shift = form.cleaned_data.get('shift')

            data = ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=course,
                location=location,
                shift=shift,
            )

            data.save()
            form = ContactForm()
            return render(request,'contact.html',{'form':form})
        else:
            return HttpResponse('form is not valid')

    else:
        form = ContactForm()
        return render(request,'contact.html',{'form':form})

def services_view(request):
    return render(request,'services.html')


import datetime as dt
date1 = dt.datetime.now()
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.method)
        if form.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date= date1,
            )

            data.save()

            feedbacks = FeedbackData.objects.all()
            form = FeedbackForm()
            my_dict = {'form':form,'feedbacks':feedbacks}
            return render(request,'feedback.html',my_dict)

    else:
        form = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        my_dict = {'form':form,'feedbacks':feedbacks}
        return  render(request,'feedback.html',my_dict)

def gallery_view(request):
    return render(request,'gallery.html')
