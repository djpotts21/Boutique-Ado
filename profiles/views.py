from django.shortcuts import render

from .models import UserProfile

def profile(request):
    '''
    Display the user's profile
    '''
    profile = UserProfile.objects.get(user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
