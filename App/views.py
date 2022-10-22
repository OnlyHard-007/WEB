from django.shortcuts import render

# Fuction to access the portfolio page
def index(requets):
     return render(requets, "index.html")
