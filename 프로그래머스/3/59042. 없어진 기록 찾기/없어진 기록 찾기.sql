SELECT animal_id, name
from animal_outs
minus
select animal_id, name
from animal_ins
