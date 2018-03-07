with year as (
    select strftime('%Y', '2018-03-01') year
)
select * 
from despesa
join year
where month >= year.year||'-01-'||'01'
and month <= year.year||'-12-'||'01'
;

