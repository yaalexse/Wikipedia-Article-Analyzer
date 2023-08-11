from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
# from rest_framework.views import APIView
from .service import Result

# This method display the page using api_view and its associated template.
# It turn out that getting the title of the request by request.GET.get('title')
# don't work with the rest of the code. The reason is that request.GET, which is
# a Dict, with parameter fixed by Django itself, is empty and so I can't access anything with it.
# Another way was found by accessing the user entry by urls.py which is named 'title' and
# pass it to the view function get_data().


@api_view(['GET'])
def get_data(request, title):
    search = Result(title)
    data = {'error message': search.error_message,
            'title': search.title,
            'summary': search.summary,
            'quotient': search.quotient}
    return Response(data)

# This method was supposed to use a Class and APIView rather than a function but it turns out
# that I wasn't able to make it work

# class GetData(APIView):
#    def get_data(self, request, *args, **kwargs):
#        search = request.GET.items()
#        data = { search }
#        return Response(data)

# The code below is for creating a page containing a search bar and a button the get the user
# request before the api view. I chosse not to continue because in the specification there is
# not any refernce to another view function except the api view.
# But if one choose to upgrade the app by making a previous page before the one displayed
# and make it more user friendly this might be the way to continue.

# def search(request):
#    search = request.GET.get('title')
#    return render(
#        request = request,
#        template_name = 'search.html',
#        context = {}
#    )
