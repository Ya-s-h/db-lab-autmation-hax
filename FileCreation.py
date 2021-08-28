import os

file_path = "dataFile"


def generate_file_name(pattern: str, number: int) -> str:
    return f"{pattern}_{number}.sql"


file_name = file_path
count = 0
valid_name = False
while valid_name is False:
    if os.path.isfile(generate_file_name(file_name, count)):
        count += 1
    else:
        valid_name = True
        file_path = generate_file_name(file_name, count)


def dataInsertion(Data: list):
    with open(file_path, "w") as fp:
        # fp.write("CREATE TABLE IF NOT EXISTS labreport(")
        # print(len(Data))
        fp.write("Insert into labreport\nvalues\n")

        for COUNT, data in enumerate(Data):
            problem_desc = data.get("problem_desc")
            assign_date = data.get("assigned_date")
            due_date = data.get("submission_date")
            mission_status = 1 if data.get("status") else 0
            fp.write(f"\t({COUNT + 1},'{problem_desc}', {assign_date}, '{due_date}', {mission_status})")
            if COUNT != len(Data) - 1: fp.write(",\n")
            else: fp.write("\n")
        fp.write(";")


if __name__ == "__main__":
    test_data = [{'assigned_date': 'NULL',
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
