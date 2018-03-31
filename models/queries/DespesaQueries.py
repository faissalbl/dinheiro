queries = {
    'add' : '''
        insert or replace into DESPESA (desc, val, paid_val, paid, month_id)
        values (:desc, :val, :paid_val, :paid, :month_id);
    ''',
    'update' : '''
        update DESPESA
        set desc = :desc,
            val = :val,
            paid_val = :paid_val,
            paid = :paid
        where id = :id;
    ''',
    'delete' : '''
        delete from DESPESA
        where id = :id;
    '''
}