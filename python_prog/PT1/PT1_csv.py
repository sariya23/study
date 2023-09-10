import csv
import pandas as pd


class CSVHelper:
    def a(self):
        imported_data = []
        with open("E.csv", 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                imported_data.append(row)

        new_row = ["Новое значение1", "Новое значение2", "Новое значение3"]
        imported_data.append(new_row)

        imported_data[1][1] = "Измененное значение"

        del imported_data[2]

        with open("E.csv", 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in imported_data:
                csv_writer.writerow(row)

    def xlsx_to_csv(self, input_xlsx_file, output_csv_file):
        df = pd.read_excel(input_xlsx_file)
        df.to_csv(output_csv_file, index=False)

    def csv_to_xlsx(self, input_csv_file, output_xlsx_file):
        df = pd.read_csv(input_csv_file)
        df.to_excel(output_xlsx_file, index=False)

    def b(self):
        self.xlsx_to_csv('D.xlsx', 'E.csv')
        self.csv_to_xlsx('E.csv', 'E_converted.xlsx')

