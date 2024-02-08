def read_records(record_file_path, header=True):

    f_reader = open(record_file_path, "r")
    records = f_reader.readlines()
    f_reader.close()

    return records

def clean_records(records):

    number_of_records = len(records)
    index = 0
    while index < number_of_records:
        records[index] = records[index].strip()
        index += 1

    return records

def show_record(record, header=None):
    if header:
        header_line = format_record(header)
        print(header_line)

    record = format_record(record)
    print(record)

def format_record(record):
    record_list = record.split(",")
    formatted_record = " | ".join(record_list)
    return formatted_record

record_file = r"D:\workspace\github\python_classroom\classrooms\basics\beme_records.txt"
beme_records = read_records(record_file, header=True)
beme_records = clean_records(beme_records)
header = beme_records[0]

first_record = beme_records[1]
show_record(first_record, header=header)
# print(beme_records)
