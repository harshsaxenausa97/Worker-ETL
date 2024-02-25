# example queries, will be different across different db platform

sqlserver_extract = ('''
  SELECT WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT
  FROM worker
''')

sqlserver_insert = ('''
  INSERT INTO worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT)
  VALUES (?, ?, ?, ?, ?, ?)  
''')

mysql_extract = ('''
  SELECT WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT
  FROM worker
''')

mysql_insert = ('''
  INSERT INTO worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT)
  VALUES (?, ?, ?, ?, ?, ?)  
''')


# exporting queries
class SqlQuery:
    def __init__(self, extract_query, load_query):
        self.extract_query = extract_query
        self.load_query = load_query


# create instances for SqlQuery class
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)
mysql_query = SqlQuery(mysql_extract, mysql_insert)

# store as list for iteration
sqlserver_queries = [sqlserver_query]
mysql_queries = [mysql_query]