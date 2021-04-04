from . models import Uservisited

def save_user(view_func):
	def wrap(request, *args, **kwargs):
		
		user = request.user
		path = request.get_full_path_info()
		url = 'http://127.0.0.1:8006'+str(path)
		Uservisited.objects.create(user=user,url=url)
		print(user,'111111111', url)
		return view_func(request, *args, **kwargs)

	return wrap