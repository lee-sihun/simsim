from tracemalloc import start
import check as ch
import server

conn = server.db_connect()

check_text = '!가르치기 '
similar_value = 0.7

start_list = []
end_list = []


def update_list(list1, list2):
    data = server.search_data(conn)
    list1.clear()
    list2.clear()
    for i in range(len(data)):
        list1.append(data[i][0])
        list2.append(data[i][1])


while True:
    update_list(start_list, end_list)
    message = input()

    if message.startswith('!종료'):
        server.db_disconnect(conn)
        break

    if message.startswith('!리스트'):
        print(start_list)
        print(end_list)
        continue

    if message.startswith(check_text):
        teach_text_start = message.strip(check_text)
        print('가르칠 대답을 입력해주세요.')

        teach_text_end = input()
        # start_list.append(teach_text_start)
        # end_list.append(teach_text_end)
        server.insert_data(conn, teach_text_start, teach_text_end)
        print('대화를 가르쳤습니다.')
        continue

    check = False
    for i in range(len(start_list)-1, -1, -1):
        if ch.Similarity_Check(start_list[i], message) > similar_value:
            result = end_list[i]
            print(result)
            check = True
            break

    if check == False:
        print('잘 모르는 대화입니다.')
