create table MONTH (
    id              integer  primary key autoincrement,
    month           text     not null,
    user            text     not null
);

CREATE UNIQUE INDEX uk_month_month_user ON MONTH(month, user);
