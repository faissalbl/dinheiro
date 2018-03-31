queries = {
	'find' : '''
		select d.id, d.desc, d.val, d.paid_val, d.paid,
        d.month_id, m.month, dm.auto
		from DESPESA_MENSAL dm
        join DESPESA d
            on d.id = dm.despesa_id
        join MONTH m
            on m.id = d.month_id
        where d.month_id = :month_id
        and (:despesa_id is null or dm.despesa_id = :despesa_id)
        and (:desc is null or d.desc = :desc)
        and (:auto is null or dm.auto = :auto);
	''',
    'count' : '''
        select count(1) count
        from DESPESA_MENSAL dm
        join DESPESA d
            on d.id = dm.despesa_id
        where d.month_id = :month_id
        and (:despesa_id is null or dm.despesa_id = :despesa_id);
    ''',
    'add' : '''
        insert or replace into DESPESA_MENSAL (despesa_id, auto)
        values (:despesa_id, :auto);
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
        where d.month_id = :month_id;
    ''',
    'find_copy' : '''
        with CP_MONTH as (
            select max(month) month
            from DESPESA d
            join MONTH m
                on m.id = d.month_id
            where m.month < :month
            and m.user = :user
        )
        select d.desc, d.val, 0 paid_val, 0 paid, dm.auto
        from CP_MONTH
        join MONTH m
            on m.month = cp_month.month
            and m.user = :user
        join DESPESA d 
            on d.month_id = m.id
        join DESPESA_MENSAL dm
            on dm.despesa_id = d.id
        where dm.auto = 0;
    '''

}