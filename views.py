from django.shortcuts import render
from django.http import HttpResponse

from restless.views import Endpoint

from .models import IPAddress

def index(request):
    return render(request, 'car_tracker/index.html')

class GetIPAddresses(Endpoint):
	def get(self, request):
		return map(lambda x: {
								'name':x['car_name'],
								'ip':x['ip'],
								'time':x['last_seen']
							 }, IPAddress.get_most_recent())

class AddIPAddress(Endpoint):
	def get(self, request):
		return self.post(request)

	def post(self, request):
		name = request.META.get('HTTP_NAME')
		ip = request.META.get('HTTP_IP')

		if not name or not ip:
			return {'result': 'failure'}

		new_ip = IPAddress()
		new_ip.car_name = name
		new_ip.ip = ip

		new_ip.save()
		return {'result': 'success'}