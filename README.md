# ExportSQLTableToFile
Export a SQL table into a flat file
<pre>
usage: 
Export given table from SQL Server to a file  [-h] 
                                              --server SERVER
                                              --table TABLE
                                              [--username USERNAME]
                                              [--password PASSWORD]
                                              [--delimiter DELIMITER]
                                              [--qualifier QUALIFIER]
                                              [--file_extension FILE_EXTENSION]

optional arguments:
  -h, --help                                  show this help message and exit
  --server SERVER                             target server
  --table TABLE                               target table - fully qualified e.g. db.schema.table
  --username USERNAME                         username when server authentication is used
  --password PASSWORD                         password when server authentication is used
  --delimiter DELIMITER                       delimiter for the output file
  --qualifier QUALIFIER                       qualifier for the output file
  --file_extension FILE_EXTENSION             extention for the output file
</pre>
