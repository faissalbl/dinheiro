create table PAGAMENTO (
    despesa_id      integer  not null,
    val             real     not null,
    paid            integer  not null default 0,
    month           text     not null,
	primary key (despesa_id, month),
        foreign key (despesa_id) references DESPESA_TEMP(despesa_id)
);
