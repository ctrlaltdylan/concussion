drop table if exists questionaires;
create table questionaires (
    id integer primary key autoincrement,
    concussion_number integer,
    headache_level integer,
    nauseous_level integer,
    drowsy_level integer,
    light_sensitivity_level integer,
    noise_sensitivity_level integer,
    foggy_level integer,
    focus_level integer
);
