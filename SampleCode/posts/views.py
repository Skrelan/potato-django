from django.shortcuts import render, get_object_or_404 , redirect #get_obj or 404 
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .forms import PostForm
from .models import Post

#CRUD
def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		#if sucess
		messages.success(request,"Sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	#if request.method == "POST":
	#	print request.POST.get("content")
	#	print request.POST.get("title")
	context = {
	 "form" : form,
	}
	return render(request, "post_form.html", context)


def posts_detail(request, id):
	#instance = Post.objects.get(id=3)
	instance = get_object_or_404(Post, id=id)
	context = { 

	"title": instance.title ,
	"instance" : instance
	}
	return render(request, "post_detail.html", context)

def posts_list(request):
	#if request.user.is_authenticated():
	#	context = { "title": "Correct user" 
	#    }
	#else :
	#	context = { "title" :"Wrong user"}
	queryset= Post.objects.all()
	context = { 
	"object_list": queryset,
	"title" :"Blogs"}
	return render(request, "post_list.html", context)
	#return HttpResponse("<h1>Lists</h1>")

def posts_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		# if sucess
		messages.success(request,"<a href='#'>Update Saved</a>" ,extra_tags="html_safe")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = { 

	"title": instance.title ,
	"instance" : instance,
	"form" : form,
	}
	return render(request, "post_form.html", context)
	#we are using render to send request , template name and context but we can do more :)


def posts_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Sucessfully Deleted")
	return redirect("posts:list")



