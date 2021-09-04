# Copyright (c) 2021 Ya-s-h
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

def dataInsertion(Data: list):
    with open(file_path, "w") as fp:
        # fp.write("CREATE TABLE IF NOT EXISTS labreport(")
        # print(len(Data))
        fp.write("use myimsdb;\n")
        fp.write("truncate labreport;\n")
        fp.write("Insert into labreport\nvalues\n")

        for COUNT, data in enumerate(Data):
            problem_desc = data.get("problem_desc")
            assign_date = data.get("assigned_date")
            due_date = data.get("submission_date")
            mission_status = "Done" if data.get("status") else "Not Done"
            s = list(problem_desc)
            for i in range(len(s)):
                if s[i] == "'":
                    s[i] = '"'
                else:continue
            problem_desc = fileFormatter(listToString(s))
            fp.write(f"({COUNT + 1 }, '{problem_desc}', {assign_date}, '{due_date}', '{mission_status}')")
            if COUNT != len(Data) - 1:
                fp.write(",\n")
            else:
                fp.write("\n")
        fp.write(";\n")
    return file_path

def fileFormatter(Text : str):
    if len(Text) >= 200:
        return Text[0:10] + "..."
    else:
        return Text
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
