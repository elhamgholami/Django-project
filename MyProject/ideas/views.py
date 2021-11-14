
from django.shortcuts import render 
from .models import Tweet
from django.contrib import messages


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html' , context={})
def show_tweets(request):
    context ={}
    context['tweets']= Tweet.objects.all().order_by('-id')
    return render (request , 'pages/tweets.html',context)

def make_tweet(request):
  if request.method == "GET":
      return render(request  , 'components/form.html' )
  elif request.method == "POST":
      data=request.POST
      obj=Tweet.objects.create(category_choice=data['category_choice'], content = data['content'] ,yourname=data['name'] , yourage=data['age'],title=data['title'])
      obj.save()
      return render (request , 'results/success.html')


def delete_view(request , id):
    try:
        obj = Tweet.objects.get(id=id)
        obj.delete()
    except Tweet.DoesNotExist:
        obj  = None
    messages.error(request, 'Item was deleted successfully!')
    return render (request , 'results/delete.html')


def search_in_tweets(request):
    query = request.POST.get('yourname',None)
    if query:
        results = Tweet.objects.filter(yourname__contains=query).distinct()
    else:
      return render(request ,'results/Failure.html' )
    return render(request, 'components/searched_result.html', {'results': results})


def know_me(request):
     return render(request, 'pages/details.html')