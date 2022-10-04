import difflib


def Similarity_Check(answer, input):
    answer_bytes = bytes(answer, 'utf-8')
    input_bytes = bytes(input, 'utf-8')
    answer_bytes_list = list(answer_bytes)
    input_bytes_list = list(input_bytes)

    sm = difflib.SequenceMatcher(None, answer_bytes_list, input_bytes_list)
    similar = sm.ratio()
    return similar

print(Similarity_Check('안녕하세요','안녕하새요'))