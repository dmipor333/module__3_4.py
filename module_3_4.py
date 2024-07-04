def single_root_worlds(root_word, *other_word):
    same_words = []
    root_words = root_word.lower()
    other_words = list(other_word)
    other_words1 = [m.lower() for m in other_words]
    for i in range(len(other_words1)):
        if root_words in other_words1[i] or other_words1[i] in root_words:
            same_words.append(other_word[i])
    return same_words
result1 = single_root_worlds('Kora', 'Koran', 'koRAN', 'korm', 'KOrabl')
result2 = single_root_worlds('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)