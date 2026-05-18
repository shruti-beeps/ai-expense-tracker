from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Expense
from .forms import ExpenseForm, RegisterForm


# REGISTER PAGE
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            # auto login after register
            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# HOME PAGE
@login_required
def home(request):

    expenses = Expense.objects.filter(user=request.user)

    total = 0

    for expense in expenses:
        total += expense.amount

    return render(request, 'home.html', {
        'expenses': expenses,
        'total': total
    })


# ADD EXPENSE
@login_required
def add_expense(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        amount = request.POST.get('amount')

        # AI CATEGORY LOGIC
        if "pizza" in title.lower():
            category = "Food"

        elif "uber" in title.lower():
            category = "Travel"

        elif "movie" in title.lower():
            category = "Entertainment"

        else:
            category = "Other"

        Expense.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            category=category
        )

        return redirect('home')

    return render(request, 'add.html')


# EDIT EXPENSE
@login_required
def edit_expense(request, id):

    expense = Expense.objects.get(id=id, user=request.user)

    form = ExpenseForm(request.POST or None, instance=expense)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add.html', {'form': form})


# DELETE EXPENSE
@login_required
def delete_expense(request, id):

    expense = Expense.objects.get(id=id, user=request.user)

    expense.delete()

    return redirect('home')