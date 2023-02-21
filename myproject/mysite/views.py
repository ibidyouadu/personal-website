from django.shortcuts import render
from django.core.mail import send_mail
from datetime import date

# Create your views here.
def home(request):
    current_year = str(date.today().year)
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_subject = request.POST['contact-subject']
        contact_body = request.POST['contact-body']

        contact_body += f"\n\nFrom {contact_email}"

        if contact_name == "": # Honey pot
            send_mail(
                subject = contact_subject,
                message = contact_body,
                from_email = contact_email,
                recipient_list = ['angel.d.umana@gmail.com']
            )

        ctx = {"submitted_email": True, "current_year": current_year}

        return render(request, 'mysite/home.html', ctx)
    else:
        ctx = {"current_year": current_year}
        return render(request, 'mysite/home.html', ctx)

def archive(request):
    return render(request, 'mysite/archive.html')

def post(request):
    return render(request, 'mysite/post.html')
