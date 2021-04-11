# Regarder le moment d'écoute en fonction de la région

SELECT nom_region, moment_d_ecoute, COUNT(moment_d_ecoute)
FROM personne 
INNER JOIN foyer ON foyer.id_foyer = personne.id_foyer_id
INNER JOIN ville ON ville.id_ville = foyer.id_ville_id
INNER JOIN region ON region.id_region = ville.id_region_id
INNER JOIN ecoute_habituellement ON ecoute_habituellement.id_personne_id = personne.id_personne
INNER JOIN moment_d_écoute ON moment_d_écoute.id_moment_d_ecoute = ecoute_habituellement.id_moment_d_ecoute_id
WHERE moment_d_ecoute = 'En voiture' 
or moment_d_ecoute = 'Au réveil ou avant de vous endormir' 
or moment_d_ecoute = 'En faisant du sport ou des activités récréatives'
GROUP BY nom_region, moment_d_ecoute
ORDER BY nom_region;