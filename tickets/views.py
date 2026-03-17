from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm, TicketForm
from .models import Profile, Ticket
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role='user')
            messages.success(request, 'Konto zostało utworzone. Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return redirect('ticket_list')
    return redirect('login')

@login_required
def ticket_list(request):
    profile = request.user.profile
    if profile.role == 'user':
        tickets = Ticket.objects.filter(created_by=request.user)
    else:
        tickets = Ticket.objects.all()

    q = request.GET.get('q')
    if q:
        tickets = tickets.filter(Q(title__icontains=q) | Q(description__icontains=q))
    status = request.GET.get('status')
    if status:
        tickets = tickets.filter(status=status)
    priority = request.GET.get('priority')
    if priority:
        tickets = tickets.filter(priority=priority)

    tickets = tickets.order_by('-created_at')

    return render(request, 'tickets/ticket_list.html', {
        'tickets': tickets,
        'status_choices': Ticket.STATUS_CHOICES,
        'priority_choices': Ticket.PRIORITY_CHOICES,
        'search_query': q or '',
        'current_status': status or '',
        'current_priority': priority or '',
    })

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, 'Zgłoszenie zostało utworzone.')
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form, 'form_title': 'Nowe zgłoszenie'})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    profile = request.user.profile
    if profile.role == 'user' and ticket.created_by != request.user:
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_details.html', {'ticket': ticket})

