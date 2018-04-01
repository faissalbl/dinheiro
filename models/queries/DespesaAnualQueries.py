queries = {
	'find' : '''
        with M_YEAR as (
            select strftime('%Y', m.month) year
            from MONTH m
            where id = :month_id
        )
        select d.id id, d.desc desc, d.val val, d.paid_val paid_val, 
        d.paid paid, d.month_id month_id, m.month month
        from DESPESA_ANUAL da
        join DESPESA d
            on d.id = da.despesa_id
        join MONTH m
            on m.id = d.month_id
            and m.user = :user
        join M_YEAR
            on m_year.year = strftime('%Y', m.month)
        and (:despesa_id is null or da.despesa_id = :despesa_id);
	''',
    'count' : '''
        select count(1) count
        from DESPESA_ANUAL da
        join DESPESA d
            on d.id = da.despesa_id
        where d.month_id = :month_id
        and (:despesa_id is null or da.despesa_id = :despesa_id);
    ''',
    'add' : '''
        insert or replace into DESPESA_ANUAL (despesa_id)
        values (:despesa_id);
    ''',
    'delete' : '''
        delete from DESPESA_ANUAL
        where despesa_id = :despesa_id;
    ''',
    'sum': '''
        with year as (
            select strftime('%Y', :month) year
        )
        select sum(d.val) val
        from DESPESA_ANUAL da
        join DESPESA d
            on d.id = da.despesa_id
        join MONTH m
            on m.id = d.month_id
            and m.user = :user
        join year
        where m.month >= year.year||'-01-'||'01'
        and m.month <= year.year||'-12-'||'01';
    ''',
    'find_copy': '''
        with CP_YEAR as (
            select max(strftime('%Y', m.month)) year
            from DESPESA d
            join MONTH m
                on m.id = d.month_id
                and m.user = :user
            where strftime('%Y', m.month) < strftime('%Y', :month)
        )
        select d.desc, d.val, 0 paid_val, 0 paid 
        from CP_YEAR
        join MONTH m
            on m.month = cp_year.year||'-01-01'
            and m.user = :user
        join DESPESA d
            on d.month_id = m.id
        join DESPESA_ANUAL da
            on da.despesa_id = d.id;
    '''
}