import csv
with open("ata_entry.csv","w") as  file:
    csv_writer_obj=csv.writer(file)
    csv_writer_obj.writerow(["Name","Age","Location"])

data=[
    ["alan",25,"new york"],["bob",28,"tokyo"],["phil",30,"dubai"]
]

with open("data_entry.csv","w") as file:
    csv_writer_obj=csv.writer(file)
    csv_writer_obj.writerow(data)
