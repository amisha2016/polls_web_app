from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse



def index(request):          #displays last three questions added
    latest_question_list=Question.objects.order_by('-pub_date')[:3]
    #output= ', '.join(a.question_text for a in latest_question_list)
    #return HttpResponse(output)
    context={'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id): #displays all the choices associated with particular question
    #return HttpResponse("You are looking at question %s." %question_id)
    question=get_object_or_404(Question, id=question_id) #return error if id does not exist else return object for that particular question
    context={'question': question}
    return render(request, 'polls/detail.html', context)



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



def results(request, question_id):
    question=get_object_or_404(Question, id=question_id)
    context={'question':question}
    return render(request, 'polls/results.html', context)
