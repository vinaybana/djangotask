from django.core.exceptions import PermissionDenied 
from django.utils.deprecation import MiddlewareMixin   

class FilterIPMiddleware(MiddlewareMixin):
	# Check if client IP address is allowed
	def process_request(self, request):
		allowed_ips = ['192.168.1.18', '123.123.123.123','127.0.0.1'] # Authorized ip's
		ip = request.META.get('REMOTE_ADDR') # Get client IP address
		if ip not in allowed_ips:
			raise PermissionDenied # If user is not allowed raise Error

		# If IP address is allowed we don't do anything
		return None