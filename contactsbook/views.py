from django.shortcuts import redirect, render

from .models import Contacts

# Create your views here.
def index(request):
    contacts = Contacts.objects.all()
    search = request.GET.get('search-area')
    if search:
        contacts = Contacts.objects.filter(name__icontains=search)
    else:
        contacts = Contacts.objects.all()
        search = ''
    return render(request, 'index.html', {'contacts': contacts, 'search': search})


def new_contact(request):
    if request.method == 'POST':
        new_contact = Contacts(
            name = request.POST['name'],
            relations = request.POST['relations'],
            email = request.POST['email'],
            phone = request.POST['phone']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new-contact.html')


def contact_profile(request, pk):
    contact = Contacts.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})


def edit_contact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.relations = request.POST['relations']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})


def delete_contact(request, pk):
    contact = Contacts.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})