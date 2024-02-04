from django.shortcuts import render, redirect
from incidentdown.models import IncidentDown
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'incidentdown/index.html')

def submitincident(request):
    if request.method == 'POST':
        caller_id = request.POST.get('caller_id')
        emailAdress = request.POST.get('emailAdress')
        description = request.POST.get('description')
        comments = request.POST.get('comments')
        impact = request.POST.get('impact')
        urgency = request.POST.get('urgency')
        worknotes = request.POST.get('worknotes')
        assignment_group = request.POST.get('assignment_group')
        state = request.POST.get('state')

    incidents = IncidentDown(
        caller_id=caller_id, 
        emailAdress=emailAdress, 
        description=description, 
        comments=comments, 
        impact = impact,
        urgency = urgency,
        worknotes = worknotes,
        assignment_group = assignment_group,
        state = state,
    )

    incidents.save()
    messages.success(request, 'Incident submitted successfully.')
    return redirect('index')

