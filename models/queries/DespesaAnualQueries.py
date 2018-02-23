queries = {
	'find' : '''
		select d.id, d.desc, d.val, d.paid_val, d.paid,
        d.month, da.saved_val
		from DESPESA_ANUAL da
        join DESPESA d
            on d.id = da.despesa_id
        where d.month = :month
        and (:despesa_id is null or da.despesa_id = :despesa_id);
	''',
    'add' : '''
        insert or replace into DESPESA_ANUAL (despesa_id, saved_val)
        values (:despesa_id, :saved_val);
    ''',
    'update' : '''
        update DESPESA_ANUAL
        set saved_val = :saved_val
        where despesa_id = :despesa_id;
    ''',
    'delete' : '''
        delete from DESPESA_ANUAL
        where despesa_id = :despesa_id;
    '''
}