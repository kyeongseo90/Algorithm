SELECT O.animal_id, O.name
from animal_outs as O
where O.animal_id not in (
    select I.animal_id
    from animal_ins AS I
)