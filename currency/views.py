import requests
from django.shortcuts import render,get_object_or_404
from .models import Currency
from .forms import CurrencyForm
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def index(request): 

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            currency=form.save(commit=False)
            currency.save()

    form = CurrencyForm()

    return render(request,'currency/currency.html',{'form': form})




def test(request):
    url = 'https://v3.exchangerate-api.com/bulk/5bb97daa8620e733a15de407/USD'
    currencies = Currency.objects.all()                                                                                                                                                                   
    print(currencies)                                                                                                                                                                                     
    for currency in currencies:                                                                                                                                                                           
        currencies = Currency.objects.all()
        response = requests.get(url).json()                                                                                                                                                               
        print(type(currency.symbol))                                                                                                                                                                      
        print(str(currency.symbol))                                                                                                                                                                       
        my_new_symbol = str(currency.symbol)                                                                                                                                                              
        print(currency.value_convert)                                                                                                                                                                     
        print(type(currency.value_convert))                                                                                                                                                               
        my_new_value = float(currency.value_convert)                                                                                                                                                      
        print(my_new_value)                                                                                                                                                                               
        new_currency_response =  response['rates'][my_new_symbol]                                                                                                                                         
        print(new_currency_response)                                                                                                                                                                      
        new_overall_response = new_currency_response * my_new_value                                                                                                                                       
        print(new_overall_response)                                                                                                                                                                       
        context = {'currencies':currencies,'currency':currency, 'my_new_value': my_new_value, 'new_currency_response': new_currency_response, 'new_overall_response': new_overall_response}
        return render(request, 'currency/currency_list.html', context)
    #print(currencies)                                                                                                                                                                                    



def currency_delete(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    currency.delete()
    return redirect('currency:currency_list')