import re


def dateAssign(cursor, SerialNo: list, Date: list):
    cursor.execute("use myimsdb;")
    for i in range(len(Date)):
        cursor.execute(
            f"update labreport set assign_date = '{Date[i]}' where Sno BETWEEN {SerialNo[i][0]} and {SerialNo[i][1]};")
    print("Db Updated")


def exec_sql_file(cursor, sql_file):
    print("\n[INFO] Executing SQL script file: '%s'" % sql_file)
    statement = ""

    for line in open(sql_file):
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            # print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
            try:
                cursor.execute(statement)
            except Exception as e:
                print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))

            statement = ""
