from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
# def index(request):
#     template = loader.get_template('Home/index.html')
#     return HttpResponse( template.render({}, request))

class Index(View):
    template = 'Home/index.html'
    # template = loader.get_template('Home/index.html')
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Home.
        """
        return render(request, self.template, self.context)


class About(View):
    """
        About me page.
    """
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)

# def Home(request):
#     context = {"message":"hola"}
#   #  template = loader.get_template('/cover/index.html')
#     return render(request, '/Home/index.html', context)
#     #return HttpResponse(template.render(request))
