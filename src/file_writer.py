import csv
import os
import logging

# -----------------------------------------------------------
# File name: file_writer.py
# Author: Anand Devarajan
# Date created: 1/04/2022
# Date last modified: 3/04/2022
# Python Version: >3.6
# -----------------------------------------------------------


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class FileWriter:

    def write_csv(self, data, ext, location):
        """ write the json file as csv in the given file path"""

        # check the file path exist exits, if not create it
        file_path = create_directory(location)

        # save the data as csv
        if ext.lower() == 'csv':
            try:
                with open(file_path, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                    writer.writeheader()
                    for data in data:
                        writer.writerow(data)
                print(f'Saving file as {file_path}')
            except IOError as e:
                logging.error(e)
        else:
            logging.error("File format not supported. Please try csv.")


def create_directory(location):
    """ check the file path exist given in the location attribute exits, if not create it """
    dir_path = os.path.dirname(__file__)
    head_tail = os.path.split(location)
    path = os.path.join(dir_path, head_tail[0])
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    file_path = os.path.join(path, location)
    return file_path
