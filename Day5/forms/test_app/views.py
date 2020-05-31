from django.template import RequestContext
from django.shortcuts import render 
from .models import Category,Page


def index(request):

    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = category.name.replace(' ', '_')

    print(category.url)
    return render(request,'test_app/index.html', context_dict)

def category(request, category_name_url):
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request,'test_app/category/python.html', context_dict)



from test_app.forms import CategoryForm

def add_category(request):

    # A HTTP POST?
    if(request.method == 'POST'):
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    return render(request,'test_app/add_category.html', {'form': form})