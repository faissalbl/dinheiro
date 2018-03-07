insert into despesa (desc, val, paid_val, paid, month)
with cp_month as (
    select max(month) month
    from despesa
    where month < '2018-06-01'
)
select desc, val, 0 paid_val, 0 paid, '2018-06-01' month 
from cp_month
join despesa 
    on despesa.month = cp_month.month
;

select * from despesa;

insert into despesa (desc, val, paid_val, paid, month)
select 'desp 4', 500, 0, 0, '2018-04-01';

delete from despesa where desc = 'desp 4' and val = 500;
