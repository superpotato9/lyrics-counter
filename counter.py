import lyr
import random
import matplotlib.pyplot as plt
def music_sorter(query):
    #prepping name and lyrics 
    lyrics = lyr.lyrics(query)
    split_lyrics = lyrics.lower().split()

    #counting it all
    split_count = []
    split_final = []
    for word in split_lyrics:
        if word not in split_final:
            split_count.append(split_lyrics.count(word))
            split_final.append(word)

    #creating dict
    count = dict(zip(split_final, split_count))

    #printing it

    dic = {}
    count_sorted = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    #count_sorted = conversion(count_sorted, dic)
    return count_sorted


def grapher(input1 = (input('what song should i use don\'t worry about caps: ')), input2 = int(input("how many of the top values should i show (dont go past 50)"))):
    show_str = input2
    how_many = int(show_str)
    ccolor = []
    key = music_sorter(input1)
    key_list = list(key.keys())
    value_list = list(key.values())
    pie_keys = []
    pie_colors = []
    pie_values = []
    for i in range(1, how_many):
        pie_keys.append(value_list[i])
    
    cbool = True
    for i in range(1, how_many):
        pie_values.append(key_list[i])
        cbool = not cbool
        if cbool == True:
            pie_colors.append('red')
        else:
            pie_colors.append("blue")
    print(key)

    plt.pie(pie_keys, labels = pie_values, colors=pie_colors, 
            startangle=90, shadow = True, normalize=True,
            radius = 1.2, autopct = '%1.1f%%')
      
    # plotting legend
    plt.legend()
      
    # showing the plot
    plt.show()


