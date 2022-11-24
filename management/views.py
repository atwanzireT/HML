from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

# def contact(request):
#     form = ContactForm(request.POST)
#     if request.method == 'POST': # check post
#         if form.is_valid():
#             data = ContactMessage() #create relation with model
#             data.name = form.cleaned_data['name'] # get form input data
#             data.email = form.cleaned_data['email']
#             data.subject = form.cleaned_data['subject']
#             data.message = form.cleaned_data['message']
#             data.ip = request.META.get('REMOTE_ADDR')
#             data.save()  #save data to table
#             return HttpResponseRedirect('/contact/')
#     form = ContactForm
#     dic = {
#         'form':form,
#     }
#     return render(request, 'contact.html', dic)