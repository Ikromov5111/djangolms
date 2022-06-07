from django.shortcuts import render
from django.http import JsonResponse
from .models import QuestionQuiz,CourseQuiz
# Create your views here.


def courseView(request):
    courses = CourseQuiz.objects.all()
    context = {
        'courses' : courses
    }
    return render(request, 'quizapp/quiz.html', context)


def api_question(request,id):
    raw_questions = QuestionQuiz.objects.all().filter(course = id)[:20]
    questions = []
    
    for raw_question in raw_questions :
        question = {}
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer1
        
        options = []
        
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        options.append(raw_question.option_three)
        options.append(raw_question.option_four)

        question['options'] = options
        
        questions.append(question)

    return JsonResponse(questions,safe=False)
def take_quiz(request, pk):
    context = {
        "id" : pk
    }
    return render(request, 'quizapp/teke_quiz.html', context)


