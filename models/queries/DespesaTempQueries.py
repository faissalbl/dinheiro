queries = {
	'find' : '''
		select d.id, d.desc, d.val, d.paid_val, d.paid,
        d.month_id, m.month, dt.months, dt.paid_months
		from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        join MONTH m
            on m.id = d.month_id
            and m.user = :user
        where ( 
            exists (
                select p.despesa_id
                from PAGAMENTO p
                where p.despesa_id = dt.despesa_id
                and p.month = :month
            )
            or d.month_id = :month_id
        )
        and (:despesa_id is null or dt.despesa_id = :despesa_id)
        order by m.month;
	''',
    'count' : '''
        select count(1) count
        from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        where ( 
            exists (
                select p.despesa_id
                from PAGAMENTO p
                where p.despesa_id = dt.despesa_id
                and p.month = :month
            )
            or d.month_id = :month_id
        )
        and exists (
            select 1
            from MONTH 
            where id = d.month_id
            and user = :user
        )
        and (:despesa_id is null or dt.despesa_id = :despesa_id)
        order by d.month;
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
    ''',
    'sum': '''
        select sum(d.val) val
        from DESPESA_TEMP dt
        join DESPESA d
            on d.id = dt.despesa_id
        where ( 
            exists (
                select p.despesa_id
                from PAGAMENTO p
                where p.despesa_id = dt.despesa_id
                and p.month = :month
            )
            or d.month_id = :month_id
        )
        and exists (
            select 1
            from MONTH 
            where id = d.month_id
            and user = :user
        )
        ;
    '''
}