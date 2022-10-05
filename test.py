from cgi import test
import server

conn = server.db_connect()
result = server.search_data(conn)
server.db_disconnect(conn)

test_list = []

for i in range(len(result)):
    test_list.append(result[i][0])

print(test_list)
