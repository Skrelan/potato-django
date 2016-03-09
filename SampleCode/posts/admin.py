from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):  #refers to the "post admin" , i.e models.py
	list_display = ["__unicode__","updated","timestamp"] #what to display in row
	list_display_links = ["__unicode__"] #what to make clickable
	#list_editable = ["title"] #makes the field editable
	list_filter = ["timestamp"] #what to filter by
	search_fields = ["title","content"] #to make it searchable
	class Meta: #class meta is working like this and new operator.  
		models = Post #go to model admin options


admin.site.register(Post ,PostAdmin)