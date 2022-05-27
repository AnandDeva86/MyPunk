import csv
import os
import unittest
from src.file_writer import FileWriter

test_data = [{"id": 1, "Company": "Tesla", "model": "Model 3", "year": "2020"},
             {"id": 2, "Company": "Ford", "model": "Model T", "year": "1920"}]

file_writer = FileWriter()
path = '/test_csv.csv'


class TestFileWriter(unittest.TestCase):
    def test_file_writing_operation(self):
        file_writer.write_csv(test_data, 'csv', path)

        jsonArray = []
        with open(path, encoding='utf-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                jsonArray.append(row)
        self.assertEqual(test_data[0]['Company'], jsonArray[0]['Company'])

        # Clean the temporary file
        os.remove(path)

    def test_logging_for_wrong_format(self):
        with self.assertLogs() as captured:
            file_writer.write_csv(test_data, 'txt', path)
        self.assertEqual(len(captured.records), 1)  # check that there is only one log message
        self.assertEqual(captured.records[0].getMessage(), "File format not supported. Please try csv.")


if __name__ == '__main__':
    unittest.main()