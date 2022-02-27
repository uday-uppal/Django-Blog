from django.shortcuts import render

from blog.models import BlogModel, contact_model
from django.views.generic import ListView
# Create your views here.
def home(request):
    x=BlogModel.objects.all()
    
    context={"blogs":x}
    # blogs[]
    return render(request,"index.html",context)
def blog_detail(request,slug):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(slug=slug).first()
        context["blog_obj"]=blog_obj
    except Exception as e:
        print(e)    
    return render(request, "blog_details.html",context)
def search_view(request,form_element):    
    return render()
def contact_view(request):    
    context={}
    # x=contact_model.object.crea
    return render(request, "contact.html",context)
def about_view(request):    
    return render(request, "aboutus.html")            

class SearchView(ListView):
    model = BlogModel
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = BlogModel.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
