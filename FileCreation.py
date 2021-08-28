import os

file_path = "dataFile.sql"

if os.path.exists(file_path):
    print('file already exists')
else:
    print("Not exists... New File will be created")


def dataInsertion(Data: list):
    with open(file_path, "w+") as fp:
        # fp.write("CREATE TABLE IF NOT EXISTS labreport(")
        # print(len(Data))
        for count, dic in enumerate(Data):
            # print(count != len(Data) - 1)
            # print(dic.values())
            fp.write("Insert into labreport(")
            for countKeys, keys in enumerate(dic.keys()):

                if countKeys != len(dic) - 1:
                    fp.write("%s ," % keys)
                else:
                    fp.write("%s" % keys)
            fp.write(") values(")
            fp.write(str(count + 1) + ", ")
            for countValues, value in enumerate(dic.values()):
                if countValues != len(dic) - 1:
                    if type(value) == str:
                        fp.write("'%s' ," % value)
                    else:
                        fp.write("%s ," % value)
                else:
                    if type(value) == str:
                        fp.write("'%s'" % value)
                    else:
                        fp.write("%s" % value)
            fp.write(");\n")


if __name__ == '__main__':
    test_data = [
        {'assigned_date': 'NULL',
         'problem_desc': '1.1 Create table',
         'status': True,
         'submission_date': '2021-08-30T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '1.2 Insert records',
         'status': True,
         'submission_date': '2021-08-30T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '1.3 Update Table',
         'status': True,
         'submission_date': '2021-08-30T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '1.4 Select all records from table',
         'status': True,
         'submission_date': '2021-08-30T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '1.5 Delete rows from table',
         'status': True,
         'submission_date': '2021-08-30T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.1 Select particular records from a table.',
         'status': True,
         'submission_date': '2021-08-29T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.2 Select distinct records from a table',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.3 Delete particular records from a table',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.4 Update particular records from a table',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.5 Filter records part I',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.6 Filter records part II',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.7 Filter records - part III',
         'status': True,
         'submission_date': '2021-09-03T23:55:00'},
        {'assigned_date': 'NULL',
         'problem_desc': '2.8 Sort table in ascending order',
         'status': True,
         'submission_date': '2021-08-29T23:55:00'}]

    dataInsertion(test_data)
