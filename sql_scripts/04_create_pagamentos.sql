create table PAGAMENTO (
    despesa_id      integer  not null primary key,
    val             real     not null,
    paid            integer  not null default 0,
    month           text     not null,
        foreign key (despesa_id) references DESPESA_TEMP(despesa_id)
);
