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
    'count' : '''
        select count(1) count
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
    ''',
    'sum': '''
        select sum(d.val) val
        from DESPESA_MENSAL dm
        join DESPESA d
            on d.id = dm.despesa_id
        where d.month = :month;
    ''',
    'find_copy' : '''
        with CP_MONTH as (
            select max(month) month
            from DESPESA
            where month < :month
        )
        select d.desc, d.val, 0 paid_val, 0 paid, :month month 
        from CP_MONTH
        join DESPESA d 
            on d.month = cp_month.month
        join DESPESA_MENSAL dm
            on dm.despesa_id = d.id;
    '''

}