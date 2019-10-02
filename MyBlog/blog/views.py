from django.shortcuts import render

# Create your views here.

posts =[
    {
    'author':'Santosh',
    'title':'Hello World',
    'content':'This is first post',
    'date_posted':'27/09/2019'
    },
    {
    'author':'Shyam',
    'title':'Hello World1',
    'content':'This is first post1',
    'date_posted':'27/09/2019'
    },
    {
    'author':'Laxman',
    'title':'Hello World1',
    'content':'This is first post',
    'date_posted':'27/09/2019'
    },
]
def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'}) #title 
