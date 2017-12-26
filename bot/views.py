# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys

sys.path.insert(0, './')
import parser


def keyboard(requests):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(requests):
    rmessage = ((requests.body).decode('utf-8'))
    return_json_str = json.loads(rmessage)
    return_str = return_json_str['content']
    rmessage = return_str

    if (rmessage.find("개발자") > -1 or rmessage.find("0") > -1):
        return_str = (parser.developer())
    return JsonResponse({
        'message': {
            'text': return_str
        },
        'keyboard': {
            'type': 'text'
        }
    })

