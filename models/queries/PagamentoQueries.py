queries = {
	'find' : '''
		select d.id, d.month_id, m.month despesa_month, p.val, p.paid, p.month
		from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        join MONTH m
            on m.id = d.month_id
        join PAGAMENTO p
            on p.despesa_id = dt.despesa_id
        where d.month_id = :month_id
        and (:despesa_id is null or dt.despesa_id = :despesa_id)
        order by m.month, d.id, p.month;
	''',
    'add' : '''
        insert or replace into PAGAMENTO (despesa_id, val, paid, month)
        values (:despesa_id, :val, :paid, :month);
    ''',
    'update' : '''
        update PAGAMENTO
        set val = :val,
            paid = :paid
        where despesa_id = :despesa_id
        and month = :month;
    ''',
    'delete' : '''
        delete from PAGAMENTO
        where despesa_id = :despesa_id;
    '''
}