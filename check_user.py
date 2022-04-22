import getpass
from mysql.connector import connect
import Record

username = getpass.getuser()


def check_user(user_name):
    """Check current user is in the user_list or not.
    Not registered -> False
    Registered -> True
    """
    records = connect(
        user="",
        password="",
        host='',
        port='',
    )
    cursor = records.cursor()
    check_user_syn = (
        "select * from all_users.user_list "
        "where User_Name like \'{0}\';".format(user_name)
    )
    cursor.execute(check_user_syn)
    out = []
    for x in cursor:
        out.append(x)  # if 'out' is noting, means not found record
    records.close()
    cursor.close()
    if not out:
        # if 'out' is an empty list, return false
        return False
    else:
        return True


def user_initialization(user_name):
    """Add user into all_users.user_list.
    Create database called user_id_username.
    Create a table in that database.
    """
    # Add user into all_users.user_list.
    add_user_syn = (
        "insert into all_users.user_list ("
        "User_Name"
        ") "
        "values("
        "\'{0}\'"
        "); ".format(user_name)
    )
    Record.execution(add_user_syn)

    user_id = Record.get_user_id(user_name)
    database_name = "user_{0}_{1}".format(user_id, user_name)

    # Create a database with user's id and name.
    create_db_syn = (
        "create database {0}; ".format(database_name)
    )
    Record.execution(create_db_syn, alter=False, create=True)

    # Create a table in the database.
    create_table_syn = (
        "use {0}; ".format(database_name) +
        "create table work_records("
        "ID int auto_increment, "
        "Work_Name varchar(32), "
        "Created_Time datetime default current_timestamp, "
        "Total_Time float default 0, "
        "Last_Done_time timestamp default current_timestamp on update current_timestamp, "
        "Comments tinytext, "
        "primary key (ID)"
        ");"
    )
    Record.execution(create_table_syn, alter=False, create=True)
    out = "User Initialized successfully. "
    return out



