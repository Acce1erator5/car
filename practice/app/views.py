from django.shortcuts import render
from app.models import Car


# Create your views here.
def cars(request):
    if request.method == "POST":
        stamp = request.POST.get('car_stamp')
        release = request.POST.get('car_release')
        color = request.POST.get('car_color')
        mileage = request.POST.get('car_mileage')
        price = request.POST.get('car_price')

        print(stamp, release, color, mileage, price)

        if stamp:
            Car.objects.create(stamp=stamp,
                               release=release,
                               color=color,
                               mileage=mileage,
                               price=price)

    return render(request, 'form_page.html')


def func(request):
    context = {'cars': Car.objects.all()}
    return render(request, 'about_page.html', context=context)