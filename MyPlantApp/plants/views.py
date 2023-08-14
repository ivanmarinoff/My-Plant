from django.shortcuts import render, redirect

from MyPlantApp.plants.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from .models import Plant
from .templatetags.custom_tags import get_profile


# Create your views here.
def index(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    profile = get_profile()
    plants = sorted(Plant.objects.all(), key=lambda x: x.pk)

    context = {
        'plants': plants,
        'plants_len': len(plants),
        'profile': profile
    }
    return render(request, 'common/catalogue.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants = Plant.objects.all()
    # form = ProfileDetailsForm(request.GET or None, instance=profile)
    context = {
        # 'form': form,
        'profile': profile,
        'plants': plants,

    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form,
        'profile': profile,
        'profile_picture': profile.profile_picture,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    plants = Plant.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')


def plant_create(request):
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'form': form,
    }
    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
    }
    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantEditForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantDeleteForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/delete-plant.html', context)
