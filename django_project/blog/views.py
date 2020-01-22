from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Jerome Garcia',
		'title': 'First Blog',
		'content': 'Lorem ipsum dolor',
		'date_posted': 'January 22, 2020'
	},
	{
		'author': 'Jerome Garcia',
		'title': 'Second Blog',
		'content': 'Lorem ipsum dolor two',
		'date_posted': 'January 24, 2020'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})