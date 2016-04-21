from __future__ import unicode_literals

from django.db import models

class IPAddress(models.Model):
	car_name = models.CharField(max_length=50)
	ip = models.CharField(max_length=15)
	time = models.DateTimeField(auto_now=True)

	@staticmethod
	def get_most_recent():
		rows = IPAddress.objects.all().order_by('-time')
		names = set()
		ans = list()
		for r in rows:
			if r.car_name not in names:
				names.add(r.car_name)
				ans.append({'car_name':r.car_name, 'ip':r.ip, 'time':r.time})
		return ans


	def dump(self):
		return {'name': self.car_name, 'ip': self.ip, 'time': self.time}