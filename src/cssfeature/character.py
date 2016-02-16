
import pandas

class CharacterFeatures(object):

    @staticmethod
    def string_length(data, column, column_name='len(sentence)', index=True):
        cpy = data.copy()
        n_col_names = [column_name if c == column else s for c,s in enumerate(cpy.columns)]
        cpy  = cpy.apply(
            CharacterFeatures.sentence_length
            , axis='columns'
            , raw=True
            , args=(column,)
        )
        cpy.columns = n_col_names
        if index:
            cpy.set_index(n_col_names)
        return cpy

    @staticmethod
    def sentence_length(a, index):
        item_pos = (index,)
        sentence = a.item(item_pos)
        sentence_length = len(sentence)
        a.itemset(item_pos, sentence_length)
        return a


