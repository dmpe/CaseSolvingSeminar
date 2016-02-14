
import sklearn
from sklearn import feature_extraction

class ExtractorCollection(object):

    def __init__(self):
        self._init_text_feature_extraction()
        pass

    def _init_text_feature_extraction(self):
        # http://scikit-learn.org/stable/modules/feature_extraction.html
        self.tfidf_vectorizer = (
            'tfidf'
            , sklearn.feature_extraction.text.TfidfVectorizer()
        )
        pass



