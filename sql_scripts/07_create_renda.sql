create table RENDA (
    tipo_renda_id    text,
    val              real    not null default 0,
    month_id         integer    not null,
    taxable          integer default 0,
        primary key (tipo_renda_id, month_id),
        foreign key (tipo_renda_id) references TIPO_RENDA(id),
        foreign key (month_id) references MONTH(id)
);
