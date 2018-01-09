text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something."
word_list = split_words(clean_text(text))
word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] -= 1
