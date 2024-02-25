from variables import datawarehouse_name

# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'SUSHILSAXENA',
  'database': '{}'.format(datawarehouse_name),
  'user': 'sa',
  'password': 'Sandreas@97',
  'autocommit': True,
}

sqlserver_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'SUSHILSAXENA',
  'database': '{}'.format(datawarehouse_name),
  'user': 'sa',
  'password': 'Sandreas@97',
  'autocommit': True,
}

# mysql
mysql_db_config = [
  {
    'user': 'root',
    'password': 'Sandreas@97',
    'host': 'localhost',
    'database': 'ORG',
  }
]