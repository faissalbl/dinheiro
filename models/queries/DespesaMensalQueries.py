queries = {
	'find' : '''
		select d.id, d.desc, d.val, d.paid_val, d.paid,
        d.month
		from DESPESA_MENSAL dm
        join DESPESA d
            on d.id = dm.despesa_id
        where d.month = :month
        and (:despesa_id is null or dm.despesa_id = :despesa_id);
	''',
    'add' : '''
        insert or replace into DESPESA_MENSAL (despesa_id)
        values (:despesa_id);
    ''',
    'delete' : '''
        delete from DESPESA_MENSAL
        where despesa_id = :despesa_id;
    '''
}