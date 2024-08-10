def count_substring(string, sub_string):
    count = 0
    for i in range(0, string.__len__() - sub_string.__len__()+1):
        if string[i:i + sub_string.__len__()] == sub_string:
            count = count + 1

    print(count)



count_substring("ABCDCDC", "CDC")