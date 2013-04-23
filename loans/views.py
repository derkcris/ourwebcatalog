from loans.models import Dependency, People
from catalog.models import Item, STATE_AVAILABLE
from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget
from datetime import date


def index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'dependency_index.html', context)


def loan_availables(request):
    items_availables = Item.objects.filter(state=STATE_AVAILABLE).order_by('-name')
    context = {
        'items_availables': items_availables,
    }
    return render(request, 'loan_availables.html', context)


def loan_add(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    peoples = People.objects.all().order_by('-last_name')
    end_date_widget = SelectDateWidget()
    today = date.today()
    end_date_render = end_date_widget.render('end_date',
                                             today)
    context = {
        'item': item,
        'peoples': peoples,
        'end_date_widget': end_date_render,
        'today': today,
    }
    return render(request, 'loan_add.html', context)


def loan_save(request, item_id):
    context = {
    }
    return render(request, 'loan_add.html', context)


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
    error_message = []

    if(dependency_id == 0 or dependency_id == '0'):
        dependency = Dependency()
    else:
        dependency = get_object_or_404(Dependency, pk=dependency_id)
    dependency.name = request.POST['name']
    dependency.description = request.POST['description']

    if len(dependency.name) == 0:
        error = True
        error_message.append("Name is required")

    if error:
        context = {
            'dependency': dependency,
            'error_message': error_message,
        }
        return render(request, 'dependency_add.html', context)
    else:
        dependency.save()
        context = {
            'dependency': dependency,
            'success_message': 'The dependency ' + dependency.name + ' has been saved.',
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


def people_index(request):
    peoples = People.objects.all().order_by('-last_name')
    context = {
        'peoples': peoples,
    }
    return render(request, 'people_index.html', context)


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
    error_message = []
    try:
        if(people_id == 0 or people_id == '0'):
            people = People()
            people.active_loans = 0
        else:
            people = get_object_or_404(People, pk=people_id)
        people.first_name = request.POST['first_name']
        people.last_name = request.POST['last_name']
        people.email = request.POST['email']
        active = request.POST['active']

        if len(people.first_name) == 0:
            error = True
            error_message.append("First name is required")

        if len(people.last_name) == 0:
            error = True
            error_message.append("Last name is required")

        if active:
            people.active = bool(active)
        else:
            error = True
            error_message.append("Active is required")

        people.dependency = Dependency.objects.get(id=request.POST['dependency'])
        validate_email(people.email)

    except(KeyError, Dependency.DoesNotExist):
        error = True
        error_message.append("Dependency is required")

    except ValidationError:
        error = True
        error_message.append("Email has not format")

    if error:
        dependencies = Dependency.objects.all().order_by('-name')
        context = {
            'people': people,
            'error_message': error_message,
            'dependencies': dependencies,
        }
        return render(request, 'people_add.html', context)
    else:
        people.save()
        context = {
            'people': people,
            'success_message': '' + people.get_full_name() + ' has been saved.',
        }
        return render(request, 'people.html', context)


def people_remove(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    people.delete()
    peoples = People.objects.all().order_by('-category')
    context = {
        'peoples': peoples,
        'success_message': 'The people ' + people.get_full_name() + ' has been delete.',
    }
    return render(request, 'people_index.html', context)
