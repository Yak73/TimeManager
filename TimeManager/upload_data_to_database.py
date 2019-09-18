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
        if cursor.rowcount == 0:  # then INSERT

            keys, values = [], []
            # keys to fill columns in insert, values to fill values in inserty
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
            fields_str = ", ".join(keys)
            values_str = ", ".join(values)

            cursor.execute("""INSERT INTO TimeLog ({k_str}) VALUES ({v_str})
                            """.format(k_str=fields_str,
                                       v_str=values_str))
        else:  # then UPDATE
            # TODO
            tracked_date = cursor.fetchone()
            cursor.execute("""UPDATE INTO""")

        """
        data_dict['tracked_date']
        data_dict['arrival_time']
        data_dict['departure_time']
        data_dict['dinner']
        data_dict['remotely']
        data_dict['time_absense_begin'] 
        data_dict['time_absense_end'] 
        data_dict['comment'] 
        data_dict['non_appearance_reason'] 
        """
    except Exception as e:
        gen_funcs.show_error(err=e)

