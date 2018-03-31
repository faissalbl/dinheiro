create table CARNE_LEAO (
    month_id    text    primary key,
    income      real    not null default 0,
    tax         real    not null default 0,
    paid        integer not null default 0,
        foreign key (month_id) references MONTH(id)
);
