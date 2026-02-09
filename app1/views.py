from django.shortcuts import render
from django.template.defaultfilters import length

from app1.forms import PersonForm
from app1.models import Person
from .utility import password_generate, strength

# Create your views here.
def index(request):
    Saved_setttings=Person.objects.all()
    form = PersonForm(request.POST)
    generate_password= None

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            settings=form.save()
            generate_password=password_generate(uppercase=settings.uppercase,
                                                digits=settings.digits,
                                                special=settings.special,length=settings.length,
                                                )

        else:
            form=PersonForm()

    context = {
        "form": form,
        "person": Saved_setttings,
        "generate_password": generate_password,
        "score": strength,


    }
    return render(request, 'index.html', context)
