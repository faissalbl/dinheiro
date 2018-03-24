create table DESPESA_MENSAL (
    despesa_id       integer not null primary key,
    auto             integer not null default 0,
        foreign key (despesa_id) references DESPESA(id)
);
