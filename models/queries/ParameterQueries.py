queries = {
	'find' : '''
		select namespace, name, val
		from PARAMETER p
        where namespace = :namespace
        and (:name is null or name = :name);
	''',
    'add' : '''
        insert or replace into PARAMETER (namespace, name, val)
        values (:namespace, :name, :val);
    ''',
    'update' : '''
        update PARAMETER
        set val = :val
        where namespace = :namespace
        and name = :name;
    ''',
    'delete' : '''
        delete from PARAMETER
        where namespace = :namespace
        and name = :name;
    '''
}