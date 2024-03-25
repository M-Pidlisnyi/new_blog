from datetime import  datetime
from .models import Category

def default(request):
    categories_list = Category.objects.all()
    copyright_time = datetime.now()
    return {'categories_list': categories_list, 'copyright_time': copyright_time}