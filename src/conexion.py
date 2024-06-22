import cx_Oracle
try:
    connection= cx_Oracle.connect(
      user='pivi',
      password='gordito'
      
    )
except Exception as ex:
  print(ex)
