"""Файл создания базы данных"""

import sqlite3

# Имя локальной БД
DB_NAME = 'DZ_database.db'

# Создаем таблицы
with sqlite3.connect(DB_NAME) as dz_db_connection:
    sql_create_sport_rigs_table = """CREATE TABLE sport_rigs (
	id	INTEGER UNIQUE,
	owner_id	INTEGER,
	harness_id	INTEGER UNIQUE,
	main_canopy_id	INTEGER UNIQUE,
	reserve_canopy_id	INTEGER UNIQUE,
	aad_id	INTEGER UNIQUE,
	service_date	TEXT,
	PRIMARY KEY(id AUTOINCREMENT)
);"""
    sql_create_main_canopies_table = """CREATE TABLE main_canopies (
    main_canopy_id INTEGER UNIQUE,
    main_model TEXT,
    main_size INTEGER,
    main_manufacturer INTEGER,
    main_mfd TEXT,
    PRIMARY KEY(main_canopy_id),
    FOREIGN KEY (main_canopy_id) REFERENCES sport_rigs (main_canopy_id));"""

    sql_create_aad_table = """CREATE TABLE AAD (
    aad_id INTEGER,
    aad_serial_number TEXT,
    aad_manufacturer TEXT,
    aad_model TEXT,
    aad_mfd TEXT,
    aad_next_service TEXT,
    aad_valid_date text,
    primary key(aad_id),
    FOREIGN key (aad_id) REFERENCES sport_rigs (aad_id));
    """

    # dz_db_connection.execute(sql_create_sport_rigs_table)
    # dz_db_connection.execute(sql_create_main_canopies_table)
    # dz_db_connection.execute(sql_create_aad_table)

    # Скрипт для наполнения таблицы sport_rigs
    sql_sport_rigs_insert = """INSERT INTO sport_rigs (owner_id, harness_id, main_canopy_id,
    reserve_canopy_id, aad_id, service_date) VALUES (?,?,?,?,?,?)"""

    # передача данных для одной записи
    # dz_db_connection.execute(sql_sport_rigs_insert, (1, 1000, 1000, 1000, 1000, '25.05.2023'))
    # dz_db_connection.commit()

    # Передача данных из списка
    # sport_rigs_list = [(2,1001,1001,1001,1001,'24.05.2023'),
    #                    (3, 1002, 1002, 1002, 1002, '23.05.2023')]
    # for rig in sport_rigs_list:
    #     dz_db_connection.execute(sql_sport_rigs_insert, rig)
    # dz_db_connection.commit()

    # SQL скрипт для внесения данных в таблицу AAD
    sql_insert_aad = """INSERT INTO AAD (aad_id, aad_serial_number, aad_manufacturer,
    aad_model, aad_mfd, aad_next_service, aad_valid_date) VALUES (?,?,?,?,?,?,?)"""

    # Данные для заполнения таблицы AAD
    aad_list = [(1000, '0001', 'AIRTEC', 'CYPRES', '01.01.2023', '01.07.2027', '01.07.2038'),
                (1001,'0002', 'VIGIL-AERO', 'VIGIl CUATRO', '01.01.2010', '01.07.2020', '01.07.2030'),
                (1002, '0003', 'MARS', 'M2-MULTY', '01.01.2022', '-------', '01.01.2037')]

    for aad in aad_list:
        dz_db_connection.execute(sql_insert_aad, aad)
    dz_db_connection.commit()