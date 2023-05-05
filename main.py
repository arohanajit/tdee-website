from encryption import main, validate_password
from table_operation import connection_estb, add_row_uname

def create_account():
    result = main()
    while result[0]=='invalid':
        result = main()

    connection,mycur = connection_estb()
    add_row_uname(connection,mycur)
    test_values = '''select * from users'''
    mycur.execute(test_values)
    mycur.fetchall()
      

    