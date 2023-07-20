from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Question,Choice
import json
@api_view(['GET'])
def give_choices(request):
    qns=request.GET['qns']
    qns=json.loads(qns)
    choices=dict()
    for q in qns.values():
        choices[q]=[ a.choice_text for a in Question.objects.get(question_text=q).choice_set.all()]
        print(choices[q])
    print(type(choices))
    obj=json.dumps(choices)
    return JsonResponse(obj,safe=False)
    return JsonResponse(request.GET,safe=False)