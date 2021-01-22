from django.shortcuts import redirect, render

from .models import Contacts

# Criação da lógica de representação das views.
# OBS: Django traz uma nova maneira de trabalhar com as views 
# que não foi usada neste aplicação. Chamadas de, classes => generic


def index(request):
    """Def index: Mostra a view index.html, buscando em contatos os seus respectivos campos.
    Além de fazer a buscar por nome no campo search."""
    contacts = Contacts.objects.all()
    search = request.GET.get('search-area')
    if search:
        contacts = Contacts.objects.filter(name__icontains=search)
    else:
        contacts = Contacts.objects.all()
        search = ''
    return render(request, 'index.html', {'contacts': contacts, 'search': search})


def new_contact(request):
    """Def new_contact: lógica inserção no banco de dados"""
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
    """Def contact_profile: mostra os campos do contato que é passado por ID"""
    contact = Contacts.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})


def edit_contact(request, pk):
    """def edit_contact: mostra o contato através do ID e dar opção de editar, trazendo os campos preenchidos com seus respectivos dados"""
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
    """def delete: excluir os dados do banco, buscando a partir do ID passado"""
    contact = Contacts.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})