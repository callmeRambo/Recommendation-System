
import os
import baserecommender
import itembasedsimilarity
import pickletool

class ItemBasedRecommender(baserecommender.BaseRecommender):
    def __init__(self, output_file,training_data,testing_data,similarity_measure):
        baserecommender.BaseRecommender.__init__(self, output_file, similarity_measure=itembasedsimilarity.predict_cosine_improved,
                             path=os.getcwd() + '//ml-100k/', training_set=training_data,
                             predicting_set=testing_data)
        self.itemMatch = None

    def calculate_similar_items(self, n, resultFile):
        result = {}
        c = 0
        likes_item = self.transformLikes(self.likes)
        for i in likes_item.keys():
            result.setdefault(i, [])
        for item in likes_item:
            scores = self.topMatches(likes_item, item, similarity_measure=self.similarity_measure, n=n)
            result[item] = scores
        pickletool.dumpPickle(result, resultFile)

    def loadItemMatch(self, itemFile):
        self.itemMatch = pickletool.loadPickle(itemFile)

    def predict_rating(self, user, movie):
        totals = 0.0
        simSums = 0.0
        sim = 0.0
        predict = 0
        try:
            itemList = self.itemMatch[movie]
        except Exception:
            predict = 4.0
            return predict
        for other in itemList:
            if other[1] == movie:
                continue
            sim = other[0]
            sim_movie = other[1]
            if sim <= 0:
                continue
            if movie not in self.likes[user] or self.likes[user][movie] == 0:
                if other[1] in self.likes[user]:
                    totals += self.likes[user][other[1]] * sim
                    simSums += sim
        if simSums == 0:
            predict = 4.0
        else:
            predict = totals / simSums
        return predict


    def get_recommended_items(self, user):
        self.loadTraining_set()
        self.itemMatch=pickletool.loadPickle('result.pkl')
        userRatings = self.likes[user]
        scores = {}
        totalSim = {}
        for (item, rating) in userRatings.items():
            try:
                self.itemMatch[item]
            except Exception:
                continue
            for (similarity, item2) in self.itemMatch[item]:
                if similarity <= 0: continue
                if item2 in userRatings: continue
                scores.setdefault(item2, 0)
                scores[item2] += similarity * rating
                totalSim.setdefault(item2, 0)
                totalSim[item2] += similarity
        rankings = [(round(score / totalSim[item], 7), item) for item, score in scores.items()]
        rankings.sort()
        rankings.reverse()
        return rankings
