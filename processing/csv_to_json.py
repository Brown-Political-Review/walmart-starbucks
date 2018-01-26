#!/usr/bin/python

import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    if len(argv) < 3:
        print 'Proper usage: python csv_json.py input_file.csv output_file.csv f'
    input_file = argv[0]
    output_file = argv[1]
    format = argv[2]
    #
    # try:
    #     opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    # except getopt.GetoptError:
    #     print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
    #     sys.exit(2)
    # for opt, arg in opts:
    #     if opt == '-h':
    #         print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
    #         sys.exit()
    #     elif opt in ("-i", "--ifile"):
    #         input_file = arg
    #     elif opt in ("-o", "--ofile"):
    #         output_file = arg
    #     elif opt in ("-f", "--format"):
    #         format = arg
    # print input_file
    # print output_file
    read_csv(input_file, output_file, format)


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "f":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

if __name__ == "__main__":
   main(sys.argv[1:])

'''
Run the script via command line.
To print json dump

python csv-json.py -i users.csv -o users.json -f dump
To print json in pretty format

python csv-json.py -i users.csv -o users.json -f pretty
'''