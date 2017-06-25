import os
import itembasedsimilarity
class BaseRecommender:
    def __init__(self, output_file, similarity_measure, path, training_set, predicting_set):
        self.output_file = os.getcwd()+'//results/' +  output_file
        self.path = path
        self.training_set = training_set
        self.predicting_set = predicting_set
        self.likes = {}
        self.predictLikes = []
        self.movieTag = {}
        self.similarity_measure = similarity_measure

    def loadTraining_set(self):
        likes = {}
        try:
            with open(self.path + self.training_set) as train:
                for line in train:
                    (userId, movieId, rating, time) = line.split('\t')
                    likes.setdefault(userId, {})
                    likes[userId][movieId] = float(rating)
        except IOError as err:
            print('File error: ' + str(err))
        self.likes = likes

    def loadPredicting_set(self):
        likes = []
        try:
            with open(self.path + self.predicting_set) as predict:
                for line in predict:
                    (userId, movieId, rating, time) = line.split('\t')
                    movieId = movieId.replace('\r\r\n', '')
                    likes.append((userId, movieId))
        except IOError as err:
            print('File error: ' + str(err))
        self.predictLikes = likes

    def transformLikes(self, likes):
        result = {}
        for person in likes:
            for item in likes[person]:
                result.setdefault(item, {})
                result[item][person] = likes[person][item]
        return result

    def topMatches(self, likes, item, similarity_measure, n):
        if similarity_measure == itembasedsimilarity.predict_cosine_improved_tag:
            scores = [(similarity_measure(likes, item, other, self.movieTag), other) for other in likes if other != item]
        else:
            scores = [(similarity_measure(likes, item, other), other) for other in likes if other != item]
        scores.sort()
        scores.reverse()
        return scores[0:n]
