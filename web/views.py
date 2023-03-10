from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Token , Expense , Income , User
from datetime import datetime


@csrf_exempt
def submit_income(request):


    #TODO: validate data , user might be fake , amount might be ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST :
        date = datetime.now()

    Income.objects.create(user = this_user , amount=request.POST['amount'] , text = request.POST['text'],
    date =date)

    print ('im in submit expence')
    print (request.POST)

    context = {
        'satatus' : 'ok',
    }

    return JsonResponse(context , encoder=JSONEncoder)



@csrf_exempt
def submit_expense(request):


    #TODO: validate data , user might be fake , amount might be ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST :
        date = datetime.now()

    Expense.objects.create(user = this_user , amount=request.POST['amount'] , text = request.POST['text'],
    date =date)

    print ('im in submit expence')
    print (request.POST)

    context = {
        'satatus' : 'ok',
    }

    return JsonResponse(context , encoder=JSONEncoder)

