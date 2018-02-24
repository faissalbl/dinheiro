queries = {
	'find' : '''
		select d.id, d.desc, d.val, d.paid_val, d.paid,
        d.month, dt.months, dt.paid_months
		from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        where d.month = :month
        and (:despesa_id is null or dt.despesa_id = :despesa_id);
	''',
    'add' : '''
        insert or replace into DESPESA_TEMP (despesa_id, months, paid_months)
        values (:despesa_id, :months, :paid_months);
    ''',
    'update' : '''
        update DESPESA_TEMP
        set months = :months,
            paid_months = :paid_months
        where despesa_id = :despesa_id;
    ''',
    'delete' : '''
        delete from DESPESA_TEMP
        where despesa_id = :despesa_id;
    '''
}