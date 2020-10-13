from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image
class HomePage(TemplateView):
    template_name = 'page/home.html'
def contact(request):
    form = Image.objects.all()
    return render(request, 'page/contact.html', {'form': form})
