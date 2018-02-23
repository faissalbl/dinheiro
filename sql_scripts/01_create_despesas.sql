create table DESPESA (
    id              integer  primary key autoincrement,
    desc            text     not null,
    val             real     not null default 0,
    paid_val        real,
    paid            integer  not null default 0,
    month           text     not null
);
