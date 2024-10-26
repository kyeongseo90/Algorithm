select I.item_id, I.item_name, I.rarity
from item_info as I
join ( # 부모가 있고, 그 부모가 rare한 애들
    select E.item_id
    from item_tree as E
    join (
        select item_id
        from item_info
        where rarity = "RARE"
    ) as F on E.parent_item_id = F.item_id
    where E.parent_item_id is not null # 그리고 parent_item이 rare이어야 함
) as T on I.item_id = T.item_id
order by I.item_id desc