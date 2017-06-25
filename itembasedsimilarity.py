from math import sqrt

def cal_distance(likes, movie1, movie2):
    count = {};
    for movie in likes[movie1]:
        if movie in likes[movie2]:
            count[movie] = 1;
    if len(count) == 0:
        return 0;
    sum_squares = sum(
        [pow(likes[movie1][movie] - likes[movie2][movie], 2) for movie in likes[movie1] if movie in likes[movie2]])
    return (1 / (1 + sqrt(sum_squares)))


def predict_cosine_improved(likes, movie1, movie2):
    count = {}
    for i in likes[movie1]:
        if i in likes[movie2]:
            count[i] = 1
    n = len(count)
    if n == 0: return 0
    count1 = 0
    count2 = 0
    for movie in likes[movie1]:
        count1 += 1
    for movie in likes[movie2]:
        count2 += 1
    totalCount = count1 + count2 - n
    x = sqrt(sum([likes[movie1][it] ** 2 for it in count]))
    y = sqrt(sum([likes[movie2][it] ** 2 for it in count]))
    xy = sum([likes[movie1][it] * likes[movie2][it] for it in count])
    cos = xy / (x * y)
    return cos * (float(n) / float(totalCount))


def predict_cosine_improved_tag(likes, movie1, movie2, movieTags):
    common = 0
    for i in movieTags[movie1]:
        if i in movieTags[movie2]:
            common += 1
    if common >= 5:
        return 0.8
    else:
        count = {}
        for i in likes[movie1]:
            if i in likes[movie2]:
                count[i] = 1
        #print count
        n = len(count)
        if n == 0:
            return 0
        count2 = 0
        count1 = 0
        for movie in likes[movie2]:
            count2 += 1
        for movie in likes[movie1]:
            count1 += 1
        totalCount = count1 + count2 - n
        x = sqrt(sum([likes[movie1][it] ** 2 for it in count]))
        y = sqrt(sum([likes[movie2][it] ** 2 for it in count]))
        xy = sum([likes[movie1][it] * likes[movie2][it] for it in count])
        cos = xy / (x * y)
        return cos * (float(n) / float(totalCount))

