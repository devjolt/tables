from pathlib import Path
from random import randint
import time

from django.shortcuts import render
from django.views.generic import TemplateView

class RandomTable(TemplateView):
    template_name = Path('tables/tables_practise.html')
    
    def get_context_data(self, **kwargs):
        start = time.time() # Timing how long all this takes. We'll stop this timer later
        context = super().get_context_data(**kwargs) # make a context object to mess with.
       
        number1 = randint(2, 12)
        number2 = randint(2, 12)
        answer = number1 * number2
        question = f"{number1} x {number2}"

        context['table'] = number1
        context['question'] = question
        context['answer'] = answer
        return context

def SpecificTableView(request, table):
    number1 = table
    number2 = randint(2, 12)
    answer = number1 * number2
    question = f"{number1} x {number2}"

    context = {}
    context['table'] = number1
    context['question'] = question
    context['answer'] = answer

    return render(request, Path('tables/tables_practise.html'), context)


class ReportView(TemplateView):
    template_name = Path('tables/report.html')