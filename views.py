

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Observation
from .forms import ObservationForm

def observation_list(request):
    observations = Observation.objects.all()
    return render(request, 'observation_list.html', {'observations': observations})

def observation_detail(request, id):
    observation = get_object_or_404(Observation, id=id)
    return render(request, 'observation_detail.html', {'observation': observation})

def observation_create(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('observation_list')
    else:
        form = ObservationForm()
    return render(request, 'observation_form.html', {'form': form})

def observation_update(request, id):
    observation = get_object_or_404(Observation, id=id)
    if request.method == 'POST':
        form = ObservationForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            return redirect('observation_list')
    else:
        form = ObservationForm(instance=observation)
    return render(request, 'observation_form.html', {'form': form})

def observation_delete(request, id):
    observation = get_object_or_404(Observation, id=id)
    if request.method == 'POST':
        observation.delete()
        return redirect('observation_list')
    return render(request, 'observation_confirm_delete.html', {'observation': observation})
