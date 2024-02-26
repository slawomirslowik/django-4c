from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = "<br>".join(["<p>" + q.question_text + "</p>" for q in latest_question_list])
    return HttpResponse(output)

def counter(request):
    template = loader.get_template('counter.html')
    context = {}
    return HttpResponse(template.render(context, request))
