# Regarder la fréquence de téléchargement illégal en fonction des tranches d'âge

SELECT tranche_age, frequence_conso_illegale, COUNT(frequence_conso_illegale)
FROM personne
INNER JOIN consommation ON consommation.id_consommation = personne.id_consommation_id
WHERE frequence_conso_illegale != 'NULL'
GROUP BY tranche_age, frequence_conso_illegale
ORDER BY tranche_age;