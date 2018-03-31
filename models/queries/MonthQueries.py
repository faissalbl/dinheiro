queries = {
	'find' : '''
		select id, month, user
		from MONTH
        where user = :user
        and (:month is null or month = :month);
	''',
    'add' : '''
        insert or replace into MONTH (month, user)
        values (:month, :user);
    ''',
    'delete' : '''
        delete from MONTH
        where month = :month
        and user = :user;
    '''
}