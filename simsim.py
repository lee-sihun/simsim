import check as ch

check_text = '!가르치기 '
start_list = []
end_list = []

while True:
    message = input()

    if message.startswith('!break'):
        break

    # if message.startswith('!print'):
    #     print(start_list)
    #     print(end_list)
    #     continue

    if message.startswith(check_text):
        teach_text_start = message.strip(check_text)
        print('가르칠 대답을 입력해주세요.')

        teach_text_end = input()
        start_list.append(teach_text_start)
        end_list.append(teach_text_end)
        print('대화를 가르쳤습니다.')
        continue

    # if message in start_list:
    #     result = end_list[start_list.index(message)]
    #     print(result)
    # else:
    #     print('잘 모르는 대화입니다.')

    check = False
    for i in range(len(start_list)-1, -1, -1):
        if ch.Similarity_Check(start_list[i], message) > 0.7:
            result = end_list[i]
            print(result)
            check = True
            break

    if check == False:
        print('잘 모르는 대화입니다.')
