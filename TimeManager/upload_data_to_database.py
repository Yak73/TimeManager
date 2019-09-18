from TimeManager import general_functions as gen_funcs
from TimeManager import download_data_from_database as from_db


# Save data to database
def save_to_database(cursor, data_dict):
    # delete excess fields for dynamic query
    temp_dict = data_dict.copy()
    try:
        for key, value in temp_dict.items():
            if value == '00-00' or value == '':
                data_dict.pop(key)
    except Exception as e:
        gen_funcs.show_error(err=e)

    try:
        # Check exist record with the date and the user
        cursor.execute("""SELECT tracked_date FROM TimeLog 
                        WHERE username = SUSER_SNAME() AND tracked_date = '{sel_date}'
                        """.format(sel_date=data_dict['tracked_date']))
    except Exception as e:
        gen_funcs.show_error(err=e)

    if cursor.rowcount == 0:
        insert_in_db(cursor, data_dict)
    else:
        update_in_db(cursor, data_dict)


# Request to insert a record to the database
def insert_in_db(cursor, data_dict):
    try:
        columns, values = convert_fields_to_query(cursor, data_dict)

        columns_str = ", ".join(columns)
        values_str = ", ".join(values)

        cursor.execute("""INSERT INTO TimeLog ({c_str}) VALUES ({v_str})
                                    """.format(c_str=columns_str,
                                               v_str=values_str))
    except Exception as e:
        gen_funcs.show_error(err=e)


# Request to update the record to the database
def update_in_db(cursor, data_dict):
    # TODO
    try:
        columns, values = convert_fields_to_query(cursor, data_dict)
        join_str = ""
        selected_date = ""
        for column, value in zip(columns, values):
            if column != 'tracked_date':
                temp_str = "{} = {}, ".format(column, value)
                join_str += temp_str
            else:
                selected_date = value
        join_str = join_str[:-2]
        cursor.execute("""UPDATE TimeLog SET {set_str} 
                        WHERE username = SUSER_SNAME() AND tracked_date = {sel_date}
                                            """.format(set_str=join_str, sel_date=selected_date))

    except Exception as e:
        gen_funcs.show_error(err=e)


# Convert fields to use in query
def convert_fields_to_query(cursor, data_dict):
    keys, values = [], []
    # keys to fill columns, values to fill values in query
    for key, value in data_dict.items():
        if 'reason' not in key:
            keys.append(key)
            # 1 -> 'True' 0 -> 'False'
            if type(value) == bool:
                if value == 0:
                    values.append(gen_funcs.add_q('False'))
                else:
                    values.append(gen_funcs.add_q('True'))
            # 10-20 -> '10:20'
            elif 'time' in key:
                values.append(gen_funcs.add_q(gen_funcs.change_sep(value)))
            # string -> 'string'
            else:
                values.append(gen_funcs.add_q(value))
        # key: 'non_appearance_reason' -> 'id_non_appearance_reason'
        # value: name_reason -> id_reason
        else:
            id_reason = from_db.get_id_reason(cursor, value)
            keys.append('id_non_appearance_reason')
            values.append(id_reason)
    return keys, values
