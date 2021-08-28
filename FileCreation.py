import os

file_path = str(os.getcwd()) + "/dataFile.txt"

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

                    fp.write("%s ," % value)
                else:
                    fp.write("%s" % value)
            fp.write(");\n")


test_data = [{"A": "First", "a": "first"}, {"B": "Second"}, {"C": "third"}]

dataInsertion(test_data)
