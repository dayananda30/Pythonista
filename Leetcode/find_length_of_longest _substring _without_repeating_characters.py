def find_longest_substring(string: str) -> int:
    max_count = 1
    for i in range(len(string)):
        count = 1
        for j in range(i + 1, len(string)):
            if string[i] != string[j]:
                count = count + 1
                if count > max_count:
                    max_count = count
            else:
                if count > max_count:
                    max_count = count
                break
    return max_count


print(find_longest_substring("aabc"))
