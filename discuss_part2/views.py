from django.shortcuts import render


from .forms import search_day ,Form
# Create your views here.

# from .forms import search_day
# Create your views here.


def discuss(request) :

    # form = search_day()
    form2 = Form()

    # a=['a','b','c','d','c']
    # 
    if request.method =='POST' :
        form2 = Form(request.POST, request.FILES)
        if form2.is_valid() :
            stock = form2.cleaned_data['tutorial_category']

        context = {
                        'form2':form2 ,
                        'stock' : stock ,
                            }
        return render(request, 'discuss/discuss.html',context)
        
    context = {   # 'form':form ,
                    'form2':form2
                        }
    return render(request, 'discuss/discuss.html',context) 


def chat(request, pk ) :

    context = { 'pk':pk,

    }
    return render(request, 'discuss/chat.html',context)

