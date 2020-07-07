import csv

def csv_dict_reader(file_obj):

    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Result Time","Granularity Period","Object Name","Cell ID","Call Attempts"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("Perf-1-2016-10-21 13:45.csv") as f_obj:
        csv_dict_reader(f_obj)

#----------------------------------------------------------------------------------------

import csv

def csv_dict_reader(file_obj):

    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["Result Time","Granularity Period","Object Name","Cell ID","Call Attempts"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("Perf-1-2016-10-21 13:30.csv ") as f_obj:
        csv_dict_reader(f_obj)