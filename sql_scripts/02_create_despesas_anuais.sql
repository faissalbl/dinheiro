create table DESPESA_ANUAL (
    despesa_id       integer not null primary key,
    saved_val        real not null default 0,
        foreign key (despesa_id) references DESPESA(id)
);
