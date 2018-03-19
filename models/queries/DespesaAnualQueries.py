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
    'count' : '''
        select count(1) count
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
    ''',
    'sum': '''
        with year as (
            select strftime('%Y', :month) year
        )
        select sum(d.val) val
        from DESPESA_ANUAL da
        join DESPESA d
            on d.id = da.despesa_id
        join year
        where d.month >= year.year||'-01-'||'01'
        and d.month <= year.year||'-12-'||'01';
    ''',
    'find_copy': '''
        with CP_YEAR as (
            select max(strftime('%Y', month)) year
            from DESPESA
            where strftime('%Y', month) < strftime('%Y', :month)
        )
        select d.desc, d.val, 0 paid_val, 0 paid, strftime('%Y', :month)||'-01-01' month,
        da.saved_val 
        from CP_YEAR
        join DESPESA d
            on d.month = cp_year.year||'-01-01'
        join DESPESA_ANUAL da
            on da.despesa_id = d.id;
    '''
}