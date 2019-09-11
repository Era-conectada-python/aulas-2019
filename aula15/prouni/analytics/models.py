from django.db import models

uf_list = [
	(1, 'RS'),
	(2, 'SC'),
	(3, 'PR'),
]


class UfCampus(models.Model):
	uf = models.TextField(max_length=2, choices=uf_list)
	total_campus = models.IntegerField()
