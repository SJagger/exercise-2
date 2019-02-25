from django.shortcuts import render
from django.contrib.auth.decorators import login_required

posts = [
    {
        'author': 'the_learning_company',
        'title': 'Where in the World Is Carmen Sandiego?',
        'content': 'Carmen Sandiego is a series of American educational mystery video games which spawned an edutainment franchise of the same name. The game released in 1985, Where in the World Is Carmen Sandiego?, triggered both the video game series and the franchise as a whole, which has continued up to the present day. Each game of the series has a particular theme and subject, where the player must use his or her knowledge to find Carmen Sandiego or any of her innumerable henchmen.',
        'date_posted': 'March 22, 2012'
    },
    {
        'author': 'monty',
        'title': 'RWBY',
        'content': 'RWBY (pronounced "ruby") is an American anime-influenced web series and media franchise created by Monty Oum for Rooster Teeth. The show is set in the fictional world of Remnant, where young people train to become warriors (called "Huntsmen" and "Huntresses") to protect their world from monsters called Grimm. The name RWBY is derived from the four main characters\' forenames: Ruby, Weiss, Blake, and Yang, as well as their associated theme colors; Red, White, Black, and Yellow.',
        'date_posted': 'July 18, 2013'
    }
]

@login_required
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def welcome(request):
    return render(request, 'blog/welcome.html', {'title': 'Welcome!'})

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
