queries = {
	'find' : '''
		select tr.id, tr.desc, r.val, r.month
		from RENDA r
        join TIPO_RENDA tr
            on tr.id = r.tipo_renda_id
        where r.month = :month
        and (:tipo_renda_id is null or tr.id = :tipo_renda_id);
	''',
    'add' : '''
        insert or replace into RENDA (tipo_renda_id, val, month)
        values (:tipo_renda_id, :val, :month);
    ''',
    'update' : '''
        update RENDA
        set val = :val
        where tipo_renda_id = :tipo_renda_id
        and month = :month;
    ''',
    'delete' : '''
        delete from RENDA
        where tipo_renda_id = :tipo_renda_id
        and month = :month;
    '''
}