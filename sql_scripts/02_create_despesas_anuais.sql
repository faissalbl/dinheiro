create table DESPESA_ANUAL (
    despesa_id       integer not null primary key,
        foreign key (despesa_id) references DESPESA(id)
);
