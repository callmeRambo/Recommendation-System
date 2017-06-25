import math
import itembasedrecommender
import itembasedsimilarity
import itembasedevaluation


def predict(i,training_data,testing_data):
    item_rec = itembasedrecommender.ItemBasedRecommender('result.txt',training_data,testing_data,itembasedsimilarity.predict_cosine_improved_tag)
    item_rec.loadTraining_set()
    item_rec.loadPredicting_set()
    item_rec.calculate_similar_items(i,'result.pkl')
    item_rec.loadItemMatch('result.pkl')
    print(itembasedevaluation.Evaluation(testing_data,itembasedrecommender.ItemBasedRecommender('result2.txt',training_data,testing_data,similarity_measure=itembasedsimilarity.predict_cosine_improved)).evalByAccuracy())
    output = open(item_rec.output_file, 'w')
    for p in item_rec.predictLikes:
        print(p[0], p[1], item_rec.predict_rating(p[0], p[1]))
        output.write(p[0] + '\t' + p[1] + '\t' + str(item_rec.predict_rating(p[0], p[1])) + '\r\r\n')
    output.close()

if __name__ == '__main__':
    print("input the name of data set as traning set (u.data ua.base u1.base u2.base u3.base u4.base u5.base")
    training_data = '//'+input()
    print("input the name of data set as testing set (u.data ua.test u1.test u2.test u3.test u4.test u5.test")
    testing_data = '//'+input()
    print("select the size of feature matrix")
    n = int(input())
    predict(n,training_data,testing_data)
    
