from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# Function-based views
# CLass-based views


def home(request):
    items = ''.join(f'<li>{i}</li>' for i in range(4))
    html = f'''
<h1>It works!</h1>
<ul>
    {items}
</ul>
    '''

    return HttpResponse(html)
