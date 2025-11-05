from django.shortcuts import render
from .models import Project
# Create your views here.
def index(request):
    return render(request,"index.html")




def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Message from {name} ({email}): {message}")
        # يمكنك هنا حفظ البيانات في DB أو إرسال إيميل لاحقًا
        return render(request, "contact.html", {"success": True})
    