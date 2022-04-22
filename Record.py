# create, update and check existence of records in SQL database.
import mysql.connector

# In MySQL, table name is not case-sensitive
# All table names are in lowercase
# Same for database names and table aliases


def execution(sql_command, alter=True, create=False):
    """Execute the MySQL command. """
    records = mysql.connector.connect(
        user='', 
        password='', 
        host='', 
        port=''
    )
    cursor = records.cursor()
    cursor.execute(sql_command)
    out = []
    if alter:
        if not create:
            records.commit()  # When the table get altered, must use this command.
        if create:
            pass
    else:  # Condition that table is not altered
        for x in cursor:
            out.append(x)  # if out is noting, means not found record
    records.close()
    cursor.close()
    if out == [] and alter:
        out = "Altered successfully. "
    if create:
        out = "Created successfully. "
    return out


def creat_record(user_db_name, work_name, comment=""):
    """Creat a record in MySQL database table 'work_records'. """
    new_record_syn = (
        "insert into {0}.work_records ("
        "Work_Name, "
        "Comments"
        ") "
        "values("
        "\'{1}\', "
        "\'{2}\'"
        "); ".format(user_db_name, work_name, comment)
    )
    execution(new_record_syn)


def create_record_table(user_db_name, work_name):
    # Create a new tabel in the database to record the specific work
    new_table_syn = (
        "use {0}; ".format(user_db_name) +
        "create table {0} ("
        "ID int auto_increment,  "
        "Done_Time datetime default current_timestamp, "
        "Duration float default 0, "
        "primary key (ID)"
        "); ".format(work_name)
    )
    execution(new_table_syn, alter=False, create=True)


def update_line(user_database_name, work_name, duration):
    """Update the total worked time in table. """
    # Create new record in single job table.
    new_record_syn = (
        "insert into {0}.{1} ("
        "Duration"
        ") "
        "values("
        "\'{2}\'"
        "); ".format(user_database_name, work_name, duration)
    )
    execution(new_record_syn)

    # Update the record in general records table.
    update_record_syn = (
        "update {0}.work_records "
        "set Total_Time = {1} + Total_Time "
        "where Work_Name = \'{2}\'; ".format(
            user_database_name,
            duration,
            work_name
        )
    )
    execution(update_record_syn)


def update_in_all_user_list(duration, user_name):
    # Update in all_uer table
    update_in_all_user_table_syn = (
        "update all_users.user_list "
        "set Total_Time = {0} + Total_Time "
        "where User_Name = \'{1}\'".format(duration, user_name)
    )
    execution(update_in_all_user_table_syn)


def check_existence(user_database_name, work_name):
    """Check a specific work is in table or not.
    Exist -> True;
    Not Exist -> False.
    """
    check_syn = (
        "select * from {0}.work_records "
        "where Work_Name like \'{1}\';".format(
            user_database_name,
            work_name
        )
    )
    t = execution(check_syn, alter=False)
    if not t:
        return False
    else:
        return True


def read_one_data(user_database_name, work_name):
    """Read one work data form the specific table.
    return a list who's every entry is a tuple,
    every tuple is one line of record. """
    read_one_syn = (
        "select * from {0}.{1}; ".format(user_database_name, work_name)
    )

    one_data = execution(read_one_syn, alter=False)
    return one_data


def read_all_data(user_database_name):
    """Read all work data from the general table.
    return a list who's every entry is a tuple,
    every tuple is one line of record. """
    read_all_syn = (
        "select * from {0}.work_records; ".format(user_database_name)
    )
    all_data = execution(read_all_syn, alter=False)
    return all_data


def get_user_id(user_name):
    """Retrieve a specific user's id from all_users.user_list"""
    get_id_syn = (
        "select ID from all_users.user_list "
        "where User_Name like \'{0}\'; ".format(user_name)
    )
    re_id = execution(get_id_syn, alter=False)
    return re_id[0][0]


def check_space(work_name):
    """Check dose work name contain space(s)
    contain -> True
    no space -> False"""
    for i in work_name:
        if i == ' ':
            return True
    return False


def backtick_work_name(work_name):
    """Add backticks before and after work name,
    to support work name with space(s)
    """
    return '`' + work_name + '`'

