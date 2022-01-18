from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_subject = request.POST['contact-subject']
        contact_body = request.POST['contact-body']

        contact_body += "\n\nFrom %s -- %s" % (contact_name, contact_email)
        ctx = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'contact_subject': contact_subject,
            'contact_body': contact_body
        }

        send_mail(
            subject = contact_subject,
            message = contact_body,
            from_email = contact_email,
            recipient_list = ['angel.d.umana@gmail.com']
        )

        return render(request, 'mysite/home.html', ctx)
    else:
        return render(request, 'mysite/home.html')

def archive(request):
    return render(request, 'mysite/archive.html')

def post(request):
    return render(request, 'mysite/post.html')
