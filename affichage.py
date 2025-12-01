import shapefile
import fltk
from math import cos

sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile

fltk.cree_fenetre(1920, 1080)
for i in range(101):
    dep  = sf.shape(i) # Récupération de l'entrée correspondant à la Seine-et-Marne
    dep_r = sf.record(i)
    if not(len(dep_r[0][0]) == 3 and dep_r[0][0][0] == "9"):
        indexes = dep.parts
        all_points = dep.points
        points = []
        for i in range(len(all_points)):
            if i in indexes and i != 0:
                fltk.polygone(points)
                points = []
            points.append((all_points[i][0] * 80 + 500, all_points[i][1] * -80 + 4250))
        fltk.polygone(points)

fltk.attend_ev()
fltk.ferme_fenetre()