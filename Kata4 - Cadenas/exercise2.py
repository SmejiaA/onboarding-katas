name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

title = "Gravity Facts about {}".format(name)

multiline = """{0}\b
------------------------------------------\b
Planet Name: {1}\b
Gravity on {2}:""".format(title, planet, name)

union = f"{multiline} {gravity * 1000} km/s"

print(union)

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

title = "Gravity Facts about {}".format(nombre)

multiline = """{0}\b
------------------------------------------\b
Planet Name: {1}\b
Gravity on {2}:""".format(title, planeta, nombre)

union = f"{multiline} {gravedad * 1000} km/s"

print(union)