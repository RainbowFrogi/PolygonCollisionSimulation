import matplotlib.pyplot as plt
import math

# Alkuperäisen kolmion kärkipisteet (x, y)
pisteet0 = [(-1, -1), (1, 0), (-1, 1)]

# Simulaatioasetukset
g = 9.81   # Painovoiman kiihtyvyys (m/s^2)
dt = 0.1   # ajanväli (s)
angular_velocity = -1.5  # kulmanopeus (rad/s)

# Alkuperäiset nopeudet kappaleelle
vx = 4   # horisontaalinen nopeus (m/s)
vy = 8   # vertikaalinen nopeus (m/s)

for _ in range(20):
	# pura pisteet0 listasta x- ja y-koordinaatit erikseen
	xcooords0, ycoords0 = zip(*pisteet0)
	xcoords = [x for x in xcooords0]
	ycoords = [y for y in ycoords0]

	# Lisätään ensimmäinen piste uudestaan listan loppuun, jotta kolmio sulkeutuu
	xcoords.append(xcoords[0])
	ycoords.append(ycoords[0])
	plt.plot(xcoords, ycoords)

	vlx = vx # horisontaalinen nopeus pysyy vakiona
	vly = vy - g * dt # vertikaalinen nopeus laskee painovoiman vaikutuksesta

	# Lasketaan keskimääräinen nopeus tällä aikavälillä
	vx_avg = (vx + vlx) / 2
	vy_avg = (vy + vly) / 2

	# Kierroskulma tällä aikavälillä: dtheta = w * dt
	rotation_angle = angular_velocity * dt

	# Kolmion keskipiste, jonka ympäri pyöritys tehdään
	cx = sum(x for x, _ in pisteet0) / len(pisteet0)
	cy = sum(y for _, y in pisteet0) / len(pisteet0)

	# Pyöritetään jokainen kärkipiste keskipisteen ympäri
	rotated_points = []
	for x, y in pisteet0:
		x_rel = x - cx
		y_rel = y - cy

		x_rot = x_rel * math.cos(rotation_angle) - y_rel * math.sin(rotation_angle)
		y_rot = x_rel * math.sin(rotation_angle) + y_rel * math.cos(rotation_angle)

		rotated_points.append((x_rot + cx, y_rot + cy))

	pisteet0 = rotated_points

	# Siirretään kolmion kärkipisteitä keskimääräisellä nopeudella kerrottuna aikavälillä m/s * s
	dx = vx_avg * dt 
	dy = vy_avg * dt

	# Siirretään kaikki kärkipisteet laskettujen dx ja dy arvojen verran
	pisteet0 = [(x + dx, y + dy) for x, y in pisteet0]

	# Päivitetään alkunopeudet seuraavaa iteraatiota varten
	vx = vlx
	vy = vly

plt.gca().set_aspect('equal', adjustable='box')
plt.show()