from django.views.generic.base import TemplateView
from django.shortcuts import render
from my_first_app.models import Car
from my_first_app.models import Author, Profile

# Create your views here.
def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    car_list = Car.objects.all()
    context = {
        "car_list" : car_list
    }
    return render(request, "my_first_app/car_list.html", context)

class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"
    def get_context_data(self):
        car_list = Car.objects.all()
        return {
                "car_list" : car_list
            }
        

def profile_view(request, *args, **kwargs):
    profile = Profile.objects.get(id=kwargs['author_id'])
    print(profile)
    context = {
        "profile" : profile
    }
    return render(request, "my_first_app/profile.html", context)