

# Get name of current user
def get_cur_user(cursor, slice_flag=False):
    cursor.execute('SELECT suser_sname()')
    name = str(cursor.fetchone())
    if 'LESTER' in name and slice_flag:
        name = name[10:-4]
    return name


# Get all kinds of NonAppearanceReasons from database
def get_reasons(cursor):
    cursor.execute('SELECT name FROM NonAppearanceReasons')
    reasons = [str(row)[2:-4] for row in cursor.fetchall()]
    reasons.insert(0, '')
    return reasons


# Get the name of reason on id_reason
def get_name_reason(cursor, id_reason):
    cursor.execute('SELECT name FROM NonAppearanceReasons WHERE id_non_appearance_reason = {id_r}'.format(
        id_r=id_reason))
    if cursor.rowcount == 0:
        return None
    name = str(cursor.fetchone())
    return name


# Get the id of reason on name_reason
def get_id_reason(cursor, name_reason):
    cursor.execute("""SELECT TOP 1 id_non_appearance_reason FROM NonAppearanceReasons WHERE name LIKE '%{name_r}%'
                    """.format(name_r=name_reason))
    if cursor.rowcount == 0:
        return None
    id_reason = str(cursor.fetchone())
    id_reason = id_reason[1]  # '(1, )' -> '1'
    return id_reason


def get_input_data(cursor, type_interval, date_interval):
    """
        @description Выпонляет запросы на извлечение данных из БД (Таблица TimeLog)
        @param {cursor} cursor Курсор для выполнения запросов к БД
        @param {int} type_interval Тип периода: d - день, w - неделя, m - месяц
        @param {tuple(str, str) or str} date_interval Интервал дат-границ периода. ('1234-12-21', '1234-12-25')
        @returns {list(dict)} Список словарей из БД. Один словарь - одна запись
    """
    list_input_data = []
    input_data = dict()

    if type(date_interval) == str and type_interval == 'd':
        date_begin = "\'{}\'".format(date_interval)
        date_end = "\'{}\'".format(date_interval)
    elif type(date_interval) == tuple and len(date_interval) == 2 and (type_interval == 'w' or type_interval == 'm'):
        date_begin = "\'{}\'".format(date_interval[0])
        date_end = "\'{}\'".format(date_interval[1])
    else:
        raise Exception('Некорректные аргументы для функции get_input_data()')

    keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']
    select_string = ", ".join(keys)
    cursor.execute("""SELECT {select_str}
                    FROM 
                        TimeLog AS tl
                    WHERE 
                        tl.username = SUSER_SNAME() 
                        AND tl.tracked_date BETWEEN {start_date} AND {end_date}
                    """.format(select_str=select_string, start_date=date_begin, end_date=date_end))

    rows = list(cursor.fetchall())
    amount_days = len(rows)
    # if not exist record with the date(s)
    if amount_days == 0:
        return list_input_data

    for _ in range(amount_days):
        input_data = {}
        row = list(rows.pop(0))
        for value, key in zip(row, keys):
            input_data[key] = value
        input_data['reason'] = None

        # if IS NULL reason (on field: TimeLog.id_non_appearance_reason)
        if not input_data['id_non_appearance_reason']:
            list_input_data.append(input_data)
            continue
        else:
            name_reason = get_name_reason(cursor, input_data['id_non_appearance_reason'])

        # if not exist reason (on field: NonAppearanceReasons.name)
        if not name_reason:
            list_input_data.append(input_data)
            continue
        else:
            input_data['reason'] = name_reason

        list_input_data.append(input_data)

    return list_input_data
