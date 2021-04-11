# Regarder le nombre d'hommes et de femmes qui écoutent chaque type de musique

SELECT sexe, style_de_musique, COUNT(style_de_musique)
FROM personne 
INNER JOIN ecoute ON personne.id_personne = ecoute.id_personne_id
INNER JOIN musique ON ecoute.id_musique_id = musique.id_musique
GROUP BY sexe,style_de_musique
ORDER BY style_de_musique;
