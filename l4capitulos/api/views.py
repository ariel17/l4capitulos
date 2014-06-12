#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Views for api application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

import json

from facepy import GraphAPI

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

from social.apps.django_app.default.models import UserSocialAuth

from .forms import FacebookBookPostForm
from book.models import Book


@login_required
def facebook_book_post(request, book_id):
    """
    Posts a book content into Facebook timeline.
    """
    content = {'error': None, 'post_url': None, 'response': None}

    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        content['error'] = "Book %s does not exist." % book_id
        raise HttpResponseNotFound(
            json.dumps(content), content_type='application/json'
        )

    if request.method == 'GET':
        form = FacebookBookPostForm(request.GET)
        if form.is_valid():
            try:
                provider = request.user.social_auth.get(provider='facebook')
            except UserSocialAuth.DoesNotExist:
                content['error'] = 'User must be logged into Facebook.'
                return HttpResponseBadRequest(
                    json.dumps(content), content_type='application/json'
                )

            graph = GraphAPI(provider.extra_data['access_token'])
            content['response'] = graph.get(
                '%s/albums' % settings.FACEBOOK_FAN_APP_ID
            )
            # content['response'] = graph.post(
            #     path='me/feed',
            #     message='Hello world! from python script'
            # )

            return HttpResponse(
                json.dumps(content), content_type='application/json'
            )

    return HttpResponseBadRequest(
        json.dumps(content), content_type='application/json'
    )
