from django.shortcuts import render
from django.views.generic.base import View

class Index(View):
	def get(self, request):
		return render(request, "index.html")

class Top_Songs(View):
	def get(self, request):
		return render(request, "top_songs.html")