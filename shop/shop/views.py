from django.shortcuts import render

def main(reqeust):
    return render(reqeust, 'main.html')