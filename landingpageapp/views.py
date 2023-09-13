from django.shortcuts import render

# Create your views here.
def HomePageView(request):
        return render(request, 'landingpageapp/homepage.html', context={})

def PageView(request, page_name):
        return render(request, f'landingpageapp/{page_name}_page.html', context={})
