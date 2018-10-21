from django.http import JsonResponse

from neptuneapi.models.neptune_core import *

def NeptunePost(request):
    """
    API response for retrieving all posts
    """

    users = NeptuneUser.objects.all()
    print("USERS:\n")
    print(users)
    post_1 = {
      'id': 1,
      'poster_name': 'Jason Brill',
      'song_name': 'Mess',
      'artist_name': 'Lil Wayne',
      'post_caption': 'Lil Wayne back at it!',      
    }
    
    post_2 = {
      'id': 2,
      'poster_name': 'Reid Ovis',
      'song_name': 'Michelle',
      'artist_name': 'The Beatles',
      'post_caption': 'A true classic',
    }
    
    posts = {
      'posts': [post_1, post_2],
    }
    return JsonResponse(posts)
