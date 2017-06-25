from __future__ import division
import os
from math import sqrt

import itembasedrecommender
import itembasedsimilarity


class Evaluation:
    def __init__(self, testFile, rec,pathStr=os.getcwd() + '//ml-100k', userFile='/u.user'):
        self.testFile = testFile
        self.rec = rec
        self.pathStr = pathStr
        self.userFile = userFile

    def load_User_file(self):
        movie_likes = {}
        try:
            with open(self.pathStr + self.userFile) as user:
                for line in user:
                    (userId, userAge) = line.split('|')[0:2]
                    movie_likes.setdefault(userId, {})
        except IOError as err:
            print ('File error: ' + str(err))
        try:
            with open(self.pathStr + self.testFile) as t:
                for line in t:
                    (userid, itemid, rating, ts) = line.split('\t')
                    movie_likes[userid][itemid] = float(rating)
        except IOError as err:
            print ('File error: ' + str(err))
        return movie_likes

    def evalByAccuracy(self):
        sum_Of_RMSE = 0
        count_Records = 0
        sum_Of_MAE = 0
        testing_Set = self.load_User_file()
        for user in testing_Set:
           # print ("------------", user, "--------")
            L = self.rec.get_recommended_items(user)
            for Item in L:
                if Item[1] in testing_Set[user]:
                    count_Records += 1
                    df = abs(Item[0] - testing_Set[user][Item[1]])
            #        print (count_Records, ":", df)
                    sum_Of_RMSE += df ** 2
                    sum_Of_MAE += df
        RMSE = sqrt(sum_Of_RMSE / count_Records)
        MAE = sum_Of_MAE / count_Records
        return MAE, RMSE, count_Records
