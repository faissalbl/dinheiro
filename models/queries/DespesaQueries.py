queries = {
    'add' : '''
        insert or replace into DESPESA (desc, val, paid_val, paid, month)
        values (:desc, :val, :paid_val, :paid, :month);
    ''',
    'update' : '''
        update DESPESA
        set desc = :desc,
            val = :val,
            paid_val = :paid_val,
            paid = :paid
        where id = :id
        and month = :month;
    ''',
    'delete' : '''
        delete from DESPESA
        where id = :id;
    '''
}