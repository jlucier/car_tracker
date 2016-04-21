from __future__ import unicode_literals

from django.db import models

class IPAddress(models.Model):
	car_name = models.CharField(max_length=50)
	ip = models.CharField(max_length=15)
	time = models.DateTimeField(auto_now=True)

	@staticmethod
	def get_most_recent():
		return IPAddress.objects.values('car_name', 'ip').annotate(last_seen=models.Max('time'))

	def dump(self):
		return {'name': self.car_name, 'ip': self.ip, 'time': self.time}