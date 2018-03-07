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
    ''',
    'copy' : '''
        insert into despesa (desc, val, paid_val, paid, month)
        with cp_month as (
            select max(month) month
            from despesa
            where month < :month
        )
        select desc, val, 0 paid_val, 0 paid, :month month 
        from cp_month
        join despesa 
            on despesa.month = cp_month.month;
    '''
}