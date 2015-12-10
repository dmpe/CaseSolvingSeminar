
import collections
import nltk
import sqlite3
import pdb

import helper
import featx


db = sqlite3.connect('../data.sqlite3')
datareader = helper.CNeuReader(db)

data = datareader.get_results()


label_feats = collections.defaultdict(list)
for d in data:
    sentence, cNeu = d
    feats = featx.bag_of_words(sentence.split(' '))
    label_feats[cNeu].append(feats)
    pass


def split_label_feats(lfeats, split=0.75):
    train_feats = []
    test_feats = []
    for label, feats in lfeats.items():
        cutoff = int(len(feats) * split)
        train_feats.extend([(feat, label) for feat in feats[:cutoff]])
        test_feats.extend([(feat, label) for feat in feats[cutoff:]])
    return train_feats, test_feats

train_feats, test_feats = split_label_feats(label_feats)


from nltk.classify import NaiveBayesClassifier
nb_classifier = NaiveBayesClassifier.train(train_feats)
print('nb_classifier.labels() => %s' % nb_classifier.labels())

acc = nltk.classify.util.accuracy(nb_classifier, test_feats)
print('accuracy => %s' % acc)








