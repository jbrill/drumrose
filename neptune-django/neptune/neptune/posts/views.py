from django.http import JsonResponse

def NeptunePost(request):
    return JsonResponse({'foo':'bar'})
