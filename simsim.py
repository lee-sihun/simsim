import check as ch
import server

conn = server.db_connect()

check_text = '!가르치기 '
similar_value = 0.6

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
        server.insert_data(conn, teach_text_start, teach_text_end)
        print('대화를 가르쳤습니다.')
        continue

    check = False
    word_list = []
    word_sim = []
    for i in range(len(start_list)-1, -1, -1):
        if ch.Similarity_Check(start_list[i], message) > similar_value:
            word_list.append(end_list[i])
            word_sim.append(ch.Similarity_Check(start_list[i], message))

    if len(word_list) != 0:
        result = word_list[word_sim.index(max(word_sim))]
        check = True
        print(result)

    if check == False:
        print('잘 모르는 대화입니다. 가르쳐주세요.')
