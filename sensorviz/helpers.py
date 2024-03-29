import csv
import logging
import os
import datetime
import argparse

def cli_init():
    parser = argparse.ArgumentParser(
        prog='Sensorviz',
        description='Fast data visualization of embedded sensors.',
        epilog='This is the way.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()
    verbose = args.verbose

    if verbose:
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

def append_row_to_csv(file_loc, dataList):
    logging.info(f"data written to {file_loc}.")
    with open(file_loc, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(dataList)

def setup_data_file(device_name, datatypesList, folder_name="data"):
    # CSV data store file setup
    data_subdir = f'{os.getcwd()}/{folder_name}'
    if not os.path.exists(data_subdir):
        os.makedirs(data_subdir)
    data_csv_filename = "{}-{}".format(datetime.datetime.now().strftime('%y-%m-%d-%X'), device_name)
    data_csv_file_loc = f'{data_subdir}/{data_csv_filename}'
    append_row_to_csv(data_csv_file_loc, ["Timestamp", "Runtime (s)"] + datatypesList)
    return data_csv_file_loc