# count the average length of words in a set

def avg_word_len(words: set) -> float:
    total_len = sum(len(word) for word in words)
    return total_len/len(words)

if __name__=='__main__':
    words_set = {"elephant", "tiger", "zebra", "giraffe", "monkey"}

    solution = avg_word_len(words=words_set)
    print(solution)
