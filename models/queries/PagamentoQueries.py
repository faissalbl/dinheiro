queries = {
	'find' : '''
		select d.id, d.month, p.val, p.paid, p.month
		from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        join PAGAMENTO p
            on p.despesa_id = dt.despesa_id
        where d.month = :despesa_month
        and (:despesa_id is null or dt.despesa_id = :despesa_id)
        order by d.month, d.id, p.month;
	''',
    'add' : '''
        insert or replace into PAGAMENTO (despesa_id, val, paid, month)
        values (:despesa_id, :val, :paid, :month);
    ''',
    'update' : '''
        update PAGAMENTO
        set val = :val,
            paid = :paid
        where despesa_id = :despesa_id;
    ''',
    'delete' : '''
        delete from PAGAMENTO
        where despesa_id = :despesa_id;
    '''
}