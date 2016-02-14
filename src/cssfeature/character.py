

class CharacterFeatures(object):

    @staticmethod
    def string_length(data, column):
        y = data.apply(CharacterFeatures.sentence_length, axis=1, raw=True, args=(column,))
        y.columns = ['len(sentence)' if c == column else s for c,s in enumerate(y.columns)]
        return y

    @staticmethod
    def sentence_length(a, index):
        item_pos = (index,)
        sentence = a.item(item_pos)
        sentence_length = len(sentence)
        a.itemset(item_pos, sentence_length)
        return a


