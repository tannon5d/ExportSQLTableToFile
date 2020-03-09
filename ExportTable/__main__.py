import pyodbc
import argparse
import csv


def get_args():
    arg_parser = argparse.ArgumentParser('Export given table from SQL Server to a file')
    arg_parser.add_argument('--server', help='target server', required=True)
    arg_parser.add_argument('--table', help='target table - fully qualified e.g. db.schema.table', required=True)
    arg_parser.add_argument('--username', help='username when server authentication is used', required=None)
    arg_parser.add_argument('--password', help='password when server authentication is used', required=None)
    arg_parser.add_argument('--delimiter', help='delimiter for the output file', default=',', required=None)
    arg_parser.add_argument('--qualifier', help='qualifier for the output file', default='"', required=None)
    arg_parser.add_argument('--file_extension', help='extention for the output file', default='csv', required=None)

    return arg_parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    database, schema, table = args.table.split('.')
    if args.username and args.password:
        login = f';UID={args.username};PWD={args.password}'
    else:
        login = ''

    odbc_drivers = pyodbc.drivers()
    for odbc_driver in odbc_drivers:
        try:
            conn = pyodbc.connect(f'DRIVER={{{odbc_driver}}};SERVER={args.server};DATABASE={database}{login}')
            break
        except pyodbc.InterfaceError:
            continue
    else: # no break i.e. no suitable driver found
        print('No suitable odbc driver found')
        exit()

    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {database}.{schema}.{table}")

        # print([column[0] for column in cursor.description])

        with open(f'{args.table}.{args.file_extension}', 'w', newline='\r\n') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=args.delimiter, quotechar=args.qualifier)
            # write header
            csvwriter.writerow([column[0] for column in cursor.description])
            for row in cursor.fetchall():
                csvwriter.writerow(row)

            print(f'Table {args.table} exported to file {args.table}.{args.file_extension}')




    

