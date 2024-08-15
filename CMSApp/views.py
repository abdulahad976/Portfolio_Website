from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm




def index(request):
        return render(request, 'index.html')

def resume(request):
        return render(request, 'resume.html')

def projects(request):
        return render(request, 'projects.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Compose the email
            subject = f"Dear {name}, Your Information is Submitted Successfully" 
            message_body = f"""
            Thank you for contacting us!
            Your contact information is as follows:

            Name: {name}
            Email: {email}
            Phone: {phone}
            
            Message:
            {message}
            """
            from_email = 'Business Email'
            to_email = [email]

            # Send the email
            send_mail(subject, message_body, from_email, to_email, fail_silently=False)

            # Redirect or show success message
            return redirect('success_page')  # Replace with your success URL or message

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
