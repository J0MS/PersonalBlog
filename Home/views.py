from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('Home/index.html')
    return HttpResponse( template.render({}, request))

class Index(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/index.html'
    # template = loader.get_template('Home/index.html')
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        print('With class-based views')
        return render(request, self.template, self.context)

# def Home(request):
#     context = {"message":"hola"}
#   #  template = loader.get_template('/cover/index.html')
#     return render(request, '/Home/index.html', context)
#     #return HttpResponse(template.render(request))
