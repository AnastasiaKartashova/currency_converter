from __future__ import division
from django.shortcuts import render
from currency.forms import ConverterForm, get_key, s, convert_list

# Create your views here.

def converter(request):
    form = ConverterForm

    if request.method == 'POST':
        amount = request.POST.get('amount')
        current_currency = request.POST.get('current_currency')
        future_currency = request.POST.get('future_currency')

        result = float(amount) / float(current_currency) * float(future_currency)

        current_currency_name = get_key(current_currency)
        future_currency_name = get_key(future_currency)

        context = {"result": result,
                   "amount": amount,
                   "s":s,
                   "convert_list": convert_list,
                   "current_currency_name": current_currency_name,
                   "future_currency_name": future_currency_name,
                   "form": form}
        return render(request, 'converter.html', context=context)
    else:
        return render(request, 'converter.html', {'form': form})
