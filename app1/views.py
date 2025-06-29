from django.shortcuts import render,redirect
from .forms import recipe
from app1.langchain1 import func


# Create your views here.
def home(request):
    session_data=request.session.get('dish_ses_store','')
    if request.method=='POST':
        form=recipe(request.POST)
        if(form.is_valid()):
            data=form.cleaned_data['recipe_name']

            dish_data=func(data)
            request.session['dish_ses_store']=dish_data
            
            #form=recipe()
            #return redirect('/')
    else:
        form=recipe()

    context={'form':form, 'session_data':session_data}



    
    return render(request,'home.html',context)
