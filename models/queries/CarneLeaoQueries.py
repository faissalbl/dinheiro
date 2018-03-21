queries = {
	'find' : '''
		select month, income, tax, paid
		from CARNE_LEAO cn
        where cn.month = :month;
	''',
    'add' : '''
        insert or replace into CARNE_LEAO (month, income, tax)
        values (:month, :income, :tax);
    ''',
    'update' : '''
        update CARNE_LEAO
        set income = :income,
            tax = :tax,
            paid = :paid
        where month = :month;
    ''',
    'delete' : '''
        delete from CARNE_LEAO
        where month = :month;
    '''
}