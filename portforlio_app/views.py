from django.shortcuts import render, get_object_or_404, redirect
from . models import PortforlioDetail,Projects,Comment,Stack,Framework,Cv,About
from . forms import CommentForm
from django.http import FileResponse

# Create your views here.
def home(request):
    data = PortforlioDetail.objects.order_by('-id').first()
    proj = Projects.objects.order_by('-id')[:3]
    count = Projects.objects.count()
    stack = Stack.objects.all()
    frame = Framework.objects.all()
    cv = Cv.objects.all().order_by('-id').first()
    return render(request, 'home.html', {'data': data, 'proj':proj, 'count':count, 'stack':stack, 'frame':frame,'cv':cv})

def detailProjectView(request, pk):
    one_view = get_object_or_404(Projects,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.project_commented= one_view
            comment.save()
    else:
        form = CommentForm()
    comment = Comment.objects.filter(project_commented=one_view)
    return render(request, 'project_detail.html', {'one_view':one_view, 'form':form, 'comment':comment})

def projectview(request):
    pro= Projects.objects.all().order_by('-id')
    return render(request, 'projects.html', {'pro':pro})


def download(request,pk):
    document = get_object_or_404(Cv,pk=pk)
    return FileResponse(
        document.cv.open('rb'),
        as_attachment=True,
        filename=document.cv.name
    )

def about(request):
    about = About.objects.all().order_by('-id')
    return render(request, 'about.html', {'about':about})

def contact(request):
    return render(request, 'contact.html')