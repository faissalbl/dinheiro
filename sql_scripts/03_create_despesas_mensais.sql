create table DESPESA_MENSAL (
    despesa_id       integer not null primary key,
        foreign key (despesa_id) references DESPESA(id)
);
