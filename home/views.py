from django.shortcuts import redirect , render 
from .forms import Signupform,UserForm,ProfileForm
from django.contrib.auth import authenticate , login
from .models import profile
# Create your views here.
def signup(request):
    if request.method=="POST":
        form =  Signupform(request.POST)
        if form.is_vaild():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username , password = password)
            login(request,user)
            return redirect('/account/profile')
    else:
        form =  Signupform() 
    return render(request , 'registration/signup.html' , {'form':form})
def profile(request):
    profile = profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html' , {'profile':profile})



def profile_edit(request):
    profile = profile.objects.get(user=request.user)

    if request.method=="POST":
        # userform=UserForm
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm( request.POST ,request.FILES ,instance=profile)
        if userform.is_vaild() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))



    else :
        userform = UserForm( instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request , 'accounts/profile_edit.html' , {'userform' = userform , 'profileform':profileform})



     