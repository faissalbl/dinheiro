create table RENDA (
    tipo_renda_id    text,
    val              real    not null default 0,
    month            text    not null,
        primary key (tipo_renda_id, month),
        foreign key (tipo_renda_id) references TIPO_RENDA(id)
);
