queries = {
	'find' : '''
		select month_id, month, user, income, tax, paid
		from CARNE_LEAO cn
        join MONTH m
            on m.id = cn.month_id
        where cn.month_id = :month_id;
	''',
    'add' : '''
        insert or replace into CARNE_LEAO (month_id, income, tax)
        values (:month_id, :income, :tax);
    ''',
    'update' : '''
        update CARNE_LEAO
        set income = :income,
            tax = :tax,
            paid = :paid
        where month_id = :month_id;
    ''',
    'delete' : '''
        delete from CARNE_LEAO
        where month_id = :month_id;
    '''
}