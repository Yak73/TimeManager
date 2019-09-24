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


def get_input_data(cursor, date):
    date = "\'{}\'".format(date)
    keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']
    select_string = ", ".join(keys)
    cursor.execute("""SELECT {select_str}
                    FROM 
                        TimeLog AS tl
                    WHERE 
                        tl.username = SUSER_SNAME() 
                        AND tl.tracked_date = {cur_date}
                    """.format(select_str=select_string, cur_date=date))

    input_data = dict()

    # if not exist record with the date
    if cursor.rowcount == 0:
        return input_data

    row = list(cursor.fetchone())
    for value, key in zip(row, keys):
        input_data[key] = value
    input_data['reason'] = None

    # if not exist reason (on field: TimeLog.id_non_appearance_reason)
    if not input_data['id_non_appearance_reason']:
        return input_data
    else:
        name_reason = get_name_reason(cursor, input_data['id_non_appearance_reason'])

    # if not exist reason (on field: NonAppearanceReasons.name)
    if not name_reason:
        return input_data
    else:
        input_data['reason'] = name_reason

    return input_data

