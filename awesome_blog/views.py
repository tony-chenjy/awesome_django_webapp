from django.shortcuts import render
from django.shortcuts import HttpResponse
from awesome_blog import services, models

blogService = services.BlogService()


# Create your views here.
def index(request):
    # return HttpResponse("hello django")
    return render(request, "index.html", )


def list_blogs(request):
    blogs = blogService.get_list()
    return render(request, "blogs.html", {"blogs": blogs})


def get_blog(request):
    id = request.GET.get("id", None)
    blog = blogService.get(id=id)
    print(blog)
    return render(request, "blog.html", {"blog": blog})
