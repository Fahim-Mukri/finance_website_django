from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def sipcalculator(request):
    return render(request, 'sipcalculator.html')
def tax_calculator(request):
    return render(request, 'tax_calculator.html')
def expense_tracker(request):
    return render(request, 'expense_tracker.html')