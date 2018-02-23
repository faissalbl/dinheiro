create table CARNE_LEAO (
    month       text    primary key,
    income      real    not null default 0,
    tax         real    not null default 0,
    paid        integer not null default 0
);
