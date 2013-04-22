from loans.models import Dependency, People
from django.shortcuts import render, get_object_or_404


def index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'dependency_index.html', context)


def dependency_index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'dependency_index.html', context)


def dependency(request, dependency_id):
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    context = {
        'dependency': dependency,
    }
    return render(request, 'dependency.html', context)


def dependency_add(request):
    dependency = Dependency()
    context = {
        'dependency': dependency,
    }
    return render(request, 'dependency_add.html', context)


def dependency_edit(request, dependency_id):
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    context = {
        'dependency': dependency,
    }
    return render(request, 'dependency_add.html', context)


def dependency_save(request, dependency_id):
    error = False
    error_message = ''
    error_fields = []

    if(dependency_id == 0 or dependency_id == '0'):
        dependency = Dependency()
    else:
        dependency = get_object_or_404(Dependency, pk=dependency_id)
    dependency.name = request.POST['name']
    dependency.description = request.POST['description']

    if len(dependency.name) == 0:
        error = True
        error_message = "Some fields are required"
        error_fields.append('Name')

    if error:
        context = {
            'dependency': dependency,
            'error_message': error_message,
            'error_fields': error_fields,
        }
        return render(request, 'dependency_add.html', context)
    else:
        dependency.save()
        context = {
            'dependency': dependency,
            'success_message': 'The dependency ' + dependency.name + ' has been added.',
        }
        return render(request, 'dependency.html', context)


def dependency_remove(request, dependency_id):
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    dependency.delete()
    dependencies = Dependency.objects.all().order_by('-dependency')
    context = {
        'dependencies': dependencies,
        'success_message': 'The dependency ' + dependency.name + ' has been delete.',
    }
    return render(request, 'dependency_index.html', context)


def dependency_people_add(request, dependency_id):
    people = People()
    people.dependency = get_object_or_404(Dependency, pk=dependency_id)
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'people': people,
        'dependencies': dependencies,
    }
    return render(request, 'people_add.html', context)


def people(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    context = {
        'people': people,
    }
    return render(request, 'people.html', context)


def people_add(request):
    people = People()
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'people': people,
        'dependencies': dependencies,
    }
    return render(request, 'people_add.html', context)


def people_edit(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'people': people,
        'dependencies': dependencies,
    }
    return render(request, 'people_add.html', context)


def people_save(request, people_id):
    error = False
    error_message = ''
    error_fields = []
    try:
        if(people_id == 0 or people_id == '0'):
            people = People()
            people.active_loans = 0
        else:
            people = get_object_or_404(People, pk=people_id)
        people.first_name = request.POST['first_name']
        people.last_name = request.POST['last_name']
        people.email = request.POST['email']
        people.active = request.POST['active']

        if len(people.first_name) == 0:
            error = True
            error_message = "Some fields are required"
            error_fields.append('First name')

        if len(people.last_name) == 0:
            error = True
            error_message = "Some fields are required"
            error_fields.append('Last name')

        if len(people.email) == 0:
            error = True
            error_message = "Some fields are required"
            error_fields.append('Email')

        people.dependency = Dependency.objects.get(id=request.POST['dependency'])

    except(KeyError, Dependency.DoesNotExist):
        error = True
        error_message = "Some error_fields are required"
        error_fields.append('Dependency')

    if error:
        dependencies = Dependency.objects.all().order_by('-name')
        context = {
            'people': people,
            'error_message': error_message,
            'error_fields': error_fields,
            'dependencies': dependencies,
        }
        return render(request, 'people_add.html', context)
    else:
        people.save()
        context = {
            'people': people,
            'success_message': 'The people ' + people.name + ' has been added.',
        }
        return render(request, 'people.html', context)


def people_remove(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    people.delete()
    peoples = People.objects.all().order_by('-category')
    context = {
        'peoples': peoples,
        'success_message': 'The people ' + people.name + ' has been delete.',
    }
    return render(request, 'people_index.html', context)

