SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM animal_ins
WHERE name in('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id