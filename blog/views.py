from django.shortcuts import render

# SGN
def post_list(request):
    return render(request, 'blog/post_list.html', {})
