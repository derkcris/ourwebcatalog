from loans.models import Dependency, People, Loan, STATE_IN_LOAN, STATE_RETURNED, CONDITION_CHOICES
from catalog.models import Item, STATE_AVAILABLE, STATE_LENT
from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget
from datetime import date, datetime


def index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'dependency_index.html', context)


def item_availables(request):
    items_availables = Item.objects.filter(state=STATE_AVAILABLE).order_by('-name')
    context = {
        'items_availables': items_availables,
    }
    return render(request, 'item_availables.html', context)


def item_on_loan(request):
    loans_on_loan = Loan.objects.filter(state=STATE_IN_LOAN).order_by('-start_date')
    context = {
        'loans_on_loan': loans_on_loan,
    }
    return render(request, 'item_on_loan.html', context)


def item_returned(request):
    returned_loans = Loan.objects.filter(state=STATE_RETURNED).order_by('-start_date')
    context = {
        'returned_loans': returned_loans,
    }
    return render(request, 'item_returned.html', context)


def loan(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    context = {
        'loan': loan,
    }
    return render(request, 'loan.html', context)


def loan_add(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    peoples = People.objects.all().order_by('-last_name')
    loan = Loan()
    loan.start_date = date.today()
    end_date_widget = SelectDateWidget()
    end_date_render = end_date_widget.render('end_date',
                                             loan.start_date)
    context = {
        'item': item,
        'loan': loan,
        'peoples': peoples,
        'end_date_widget': end_date_render,
    }
    return render(request, 'loan_add.html', context)


def loan_save(request, item_id):
    error = False
    error_message = []

    try:
        loan = Loan()
        loan.item = get_object_or_404(Item, pk=item_id)
        loan.start_date = date.today()
        loan.end_date = None
        loan.estimated_end_date = date(int(request.POST['end_date_year']),
                                       int(request.POST['end_date_month']),
                                       int(request.POST['end_date_day']))
        loan.state = STATE_IN_LOAN
        loan.observations_loan = request.POST['observations']
        loan.people = People.objects.get(pk=request.POST['people'])

    except(KeyError, People.DoesNotExist):
        error = True
        error_message.append("La persona es requerida")

    if error:
        peoples = People.objects.all().order_by('-last_name')
        end_date_widget = SelectDateWidget()
        end_date_render = end_date_widget.render('end_date',
                                                 loan.estimated_end_date)
        context = {
            'item': loan.item,
            'loan': loan,
            'peoples': peoples,
            'end_date_widget': end_date_render,
            'error_message': error_message,
        }
        return render(request, 'loan_add.html', context)
    else:
        loan.condition_loan = loan.item.condition
        loan.condition_return = None
        loan.start_date = datetime.today()
        loan.item.state = STATE_LENT
        loan.people.active_loans = loan.people.active_loans + 1
        loan.save()
        loan.item.save()
        loan.people.save()
        context = {
            'loan': loan,
            'success_message': 'El prestamo se ha relizado exitosamente.',
        }
        return render(request, 'loan.html', context)


def loan_return(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    loan.end_date = datetime.today()
    context = {
        'loan': loan,
        'CONDITION_CHOICES': CONDITION_CHOICES,
    }
    return render(request, 'loan_return.html', context)


def loan_return_save(request, loan_id):
    error = False
    error_message = []

    loan = get_object_or_404(Loan, pk=loan_id)
    loan.condition_return = request.POST['condition_return']
    loan.observations_return = request.POST['observations_return']

    if error:
        context = {
            'loan': loan,
            'error_message': error_message,
        }
        return render(request, 'loan_return.html', context)
    else:
        loan.state = STATE_RETURNED
        loan.item.state = STATE_AVAILABLE
        loan.end_date = datetime.today()
        loan.item.condition = loan.condition_return
        loan.people.active_loans = loan.people.active_loans - 1
        loan.save()
        loan.item.save()
        loan.people.save()
        context = {
            'loan': loan,
            'success_message': 'El item ha sido devuelto exitosamente.',
        }
        return render(request, 'loan.html', context)


def dependency_index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'dependency_index.html', context)


def dependency(request, dependency_id):
    dependencies = Dependency.objects.all().order_by('-name')
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    context = {
        'dependencies': dependencies,
        'dependency': dependency,
    }
    return render(request, 'dependency.html', context)


def dependency_add(request):
    dependencies = Dependency.objects.all().order_by('-name')
    dependency = Dependency()
    context = {
        'dependencies': dependencies,
        'dependency': dependency,
    }
    return render(request, 'dependency_add.html', context)


def dependency_edit(request, dependency_id):
    dependencies = Dependency.objects.all().order_by('-name')
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    context = {
        'dependencies': dependencies,
        'dependency': dependency,
    }
    return render(request, 'dependency_add.html', context)


def dependency_save(request, dependency_id):
    dependencies = Dependency.objects.all().order_by('-name')
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
        error_message.append("El nombre es requerido")

    if error:
        context = {
            'dependencies': dependencies,
            'dependency': dependency,
            'error_message': error_message,
        }
        return render(request, 'dependency_add.html', context)
    else:
        dependency.save()
        context = {
            'dependencies': dependencies,
            'dependency': dependency,
            'success_message': 'La dependencia ' + dependency.name + ' ha sido guardada exitosamente.',
        }
        return render(request, 'dependency.html', context)


def dependency_remove(request, dependency_id):
    dependencies = Dependency.objects.all().order_by('-dependency')
    dependency = get_object_or_404(Dependency, pk=dependency_id)
    dependency.delete()
    context = {
        'dependencies': dependencies,
        'success_message': 'La dependencia ' + dependency.name + ' ha sido eliminada exitosamente.',
    }
    return render(request, 'dependency_index.html', context)


def dependency_people_add(request, dependency_id):
    dependencies = Dependency.objects.all().order_by('-name')
    people = People()
    people.dependency = get_object_or_404(Dependency, pk=dependency_id)
    context = {
        'dependencies': dependencies,
        'people': people,
    }
    return render(request, 'people_add.html', context)


def people_index(request):
    dependencies = Dependency.objects.all().order_by('-name')
    peoples = People.objects.all().order_by('-last_name')
    context = {
        'dependencies': dependencies,
        'peoples': peoples,
    }
    return render(request, 'people_index.html', context)


def people(request, people_id):
    dependencies = Dependency.objects.all().order_by('-name')
    people = get_object_or_404(People, pk=people_id)
    active_loans = Loan.objects.filter(people_id=people.id,
                                       state=STATE_IN_LOAN).order_by('-start_date')
    context = {
        'dependencies': dependencies,
        'people': people,
        'active_loans': active_loans,
    }
    return render(request, 'people.html', context)


def people_returned(request, people_id):
    dependencies = Dependency.objects.all().order_by('-name')
    people = get_object_or_404(People, pk=people_id)
    return_loans = Loan.objects.filter(people_id=people.id,
                                       state=STATE_RETURNED).order_by('-start_date')
    context = {
        'dependencies': dependencies,
        'people': people,
        'return_loans': return_loans,
    }
    return render(request, 'people_returned.html', context)


def people_add(request):
    dependencies = Dependency.objects.all().order_by('-name')
    people = People()
    context = {
        'dependencies': dependencies,
        'people': people,
    }
    return render(request, 'people_add.html', context)


def people_edit(request, people_id):
    dependencies = Dependency.objects.all().order_by('-name')
    people = get_object_or_404(People, pk=people_id)
    context = {
        'dependencies': dependencies,
        'people': people,
    }
    return render(request, 'people_add.html', context)


def people_save(request, people_id):
    dependencies = Dependency.objects.all().order_by('-name')
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
            error_message.append("El nombre es requerido")

        if len(people.last_name) == 0:
            error = True
            error_message.append("El apellido es requerido")

        if active:
            people.active = bool(active)
        else:
            error = True
            error_message.append("El campo activo es requerido")

        people.dependency = Dependency.objects.get(id=request.POST['dependency'])
        validate_email(people.email)

    except(KeyError, Dependency.DoesNotExist):
        error = True
        error_message.append("La dependencia es requerida")

    except ValidationError:
        error = True
        error_message.append("El correo no tiene un formato adecuado")

    if error:
        dependencies = Dependency.objects.all().order_by('-name')
        context = {
            'dependencies': dependencies,
            'people': people,
            'error_message': error_message,
        }
        return render(request, 'people_add.html', context)
    else:
        people.save()
        context = {
            'dependencies': dependencies,
            'people': people,
            'success_message': 'La persona ' + people.get_full_name() + ' ha sido guardado exitosamente',
        }
        return render(request, 'people.html', context)


def people_remove(request, people_id):
    dependencies = Dependency.objects.all().order_by('-name')
    people = get_object_or_404(People, pk=people_id)
    people.delete()
    peoples = People.objects.all().order_by('-category')
    context = {
        'dependencies': dependencies,
        'peoples': peoples,
        'success_message': 'La persona  ' + people.get_full_name() + ' ha sido eliminada exitosamente.',
    }
    return render(request, 'people_index.html', context)
