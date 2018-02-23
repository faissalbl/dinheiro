create table DESPESA_TEMP (
    despesa_id        integer  not null primary key,
    months            integer  not null,
    paid_months       integer  not null default 0,
        foreign key (despesa_id) references DESPESA (id)
);
