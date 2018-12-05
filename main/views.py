from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import BestTips, OurFavouritePick
from django.views import generic
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from blog.models import Post

@login_required
def contact(request):
    confirm_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            phone = form.cleaned_data['phone']
            subject = 'Message from %s - %s' % (name, phone)
            message = form.cleaned_data['message']
            print(name, emailFrom, phone, message)
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True,)

            confirm_message = 'Your Message was successfully sent! Thank you'
            form = None
            
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form, 'confirm_message': confirm_message,})


class IndexListView(generic.ListView):
    template_name = 'main/index.html'

    def get(self, request):
        tips = BestTips.objects.all().order_by('home_Percent')
        posts = Post.objects.all().order_by('-post_date')
        context = {'posts': posts, 'tips': tips}
        return render(request, self.template_name, context)



def LiveListView(request):
    return render(request, 'main/livescore.html')

class AllTipsListView(generic.ListView):
    model = BestTips
    template_name = 'main/alltips.html'
    queryset = BestTips.objects.all().order_by('kick_of_Time') 
    context_object_name = 'tips'
    paginate_by = 15

class BestTipsListView(generic.ListView):
    model = OurFavouritePick
    template_name = 'main/favourite.html'
    queryset = OurFavouritePick.objects.all().order_by('kick_of_Time') 
    context_object_name = 'favourites'
    paginate_by = 15
   