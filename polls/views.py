from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


class  IndexView(generic.ListView):          #displays last three questions added
    context_object_name='latest_question_list'
    template_name='polls/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:4]


class DetailView(generic.DetailView):
    template_name='polls/detail.html'
    model=Question

class ResultsView(generic.DetailView):
    template_name='polls/results.html'
    model=Question


def vote(request, question_id):
    question=get_object_or_404(Question, id=question_id)
    try:
        selected_choice= question.choice_set.get(id=request.POST['choice_ticked'])
    except(KeyError, Choice.DoesNotExist):
        context={'question':question, 'error_message': "You didn't select a choice"}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes+=1 #increment the vote
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

