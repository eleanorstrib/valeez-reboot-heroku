

valeez = {}

# query database depending on gender specified
if user_voyages[0].gender == "female":
	valeez_garments = list(Garment.objects.filter(temp='temp_all', female=True))
	valeez_temp_spec = list(Garment.objects.filter(temp=temp_cat, female=True))
	valeez_garments = valeez_garments + valeez_temp_spec
else:
	valeez_garments= list(Garment.objects.filter(temp='temp_all', male=True, trip_type=voyage_type))
	valeez_temp_spec = list(Garment.objects.filter(temp=temp_cat, male=True, trip_type=voyage_type))
	valeez_garments = valeez_garments + valeez_temp_spec


for item in valeez_garments:
	if item.layer == 0 or item.layer == 1:
		quantity = duration_int
	elif item.layer == 2 or item.layer == 3:
		if duration_int/2 < 1:
			quantity = 1
		else:
			quantity = int(duration_int/2)
	else:
		quantity = 1
	valeez[item.name] = quantity

toiletries = Toiletry.objects.filter(trip_duration__lte=duration_int)

for item in toiletries:
	valeez[item.name] = 1

item_count = sum(valeez.values())