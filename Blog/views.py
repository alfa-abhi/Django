from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import HttpResponseRedirect
import MySQLdb

from Blog.models import Document
from Blog.forms import DocumentForm

from django.core.urlresolvers import reverse


def index(request):
    return render_to_response("first.html")

def contact(request):
    return render(request,'contact.html')

def post(request):
    db = MySQLdb.connect("localhost","root","2801","tenma" )
    cursor = db.cursor()
    query="Select * from blog_document"
    cursor.execute(query)

    results = cursor.fetchall()
    lia=[]
    for row in results:
        location=row[1]
        urld=location.split("/")
        print(location)
        lia.append(urld[1])

    db.close()
    return render(request,'post.html', {'ima': lia})

def mess(request):
    s1=request.POST['name']
    s2=request.POST['email']
    s3=request.POST['subject']
    if s2=="":
        return render(request,"contact.html",{'receive':False})
    else:
        li=s1+"\n"+s2+"\n"+s3+"\n";
        fn=s2 + ".txt";
        file=open(fn,'a')
        file.write(li)
        file.close()
        return render(request,"contact.html",{'receive':True})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Blog.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'post.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def seppost(request):
    return render(request,'seppost.html',{'counter':0})

def login(request):
    s1=request.POST.get('username')
    s2=request.POST.get('psw')
    flag=0
    db = MySQLdb.connect("localhost","root","2801","tenma" )
    cursor = db.cursor()

    cursor.execute("Select * from blog_admin")

    results = cursor.fetchall()
    for row in results:
        usr=row[0]
        ps=row[1]
        if usr==s1:
            flag=1
            if ps==s2:
                return render(request,"post.html",{'error':False, 'counter':1})
            else:
                return render(request,"seppost.html",{'error':True})
    if flag==0:
        return render(request,"seppost.html",{'error':True})