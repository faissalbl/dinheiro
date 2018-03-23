queries = {
	'find' : '''
		select tr.id tipo_renda_id, tr.desc, r.val, r.month, r.taxable
		from RENDA r
        join TIPO_RENDA tr
            on tr.id = r.tipo_renda_id
        where r.month = :month
        and (:tipo_renda_id is null or tr.id = :tipo_renda_id)
        and (:auto is null or tr.auto = :auto)
        and (:taxable is null or r.taxable = :taxable);
	''',
    'count' : '''
        select count(1) count
        from RENDA r
        join TIPO_RENDA tr
            on tr.id = r.tipo_renda_id
        where r.month = :month
        and (:tipo_renda_id is null or tr.id = :tipo_renda_id)
        and (:auto is null or tr.auto = :auto);
    ''',
    'add' : '''
        insert or replace into RENDA (tipo_renda_id, val, month, taxable)
        values (:tipo_renda_id, :val, :month, :taxable);
    ''',
    'update' : '''
        update RENDA
        set val = :val,
            taxable = :taxable
        where tipo_renda_id = :tipo_renda_id
        and month = :month;
    ''',
    'delete' : '''
        delete from RENDA
        where tipo_renda_id = :tipo_renda_id
        and month = :month;
    '''
}