
import sklearn
from sklearn import ensemble
from sklearn import feature_extraction
from sklearn import feature_selection
from sklearn import naive_bayes
from sklearn import neighbors

class ClassifierCollection(object):
    def __init__(self):
        self._init_support_vector_machines()
        self._init_naive_bayes()
        self._init_ensemble_methods()
        self._init_neighbor_methods()
        pass

    def _init_support_vector_machines(self):
        ## Support Vector Machines
        # http://scikit-learn.org/stable/modules/svm.html
        self.svc = (
            "support vector classifier"
            , sklearn.svm.SVC(kernel='linear', C=1))
        self.linear_svc = (
            "linear svc"
            , sklearn.svm.LinearSVC(random_state = 9974))
        pass
    
    def _init_naive_bayes(self):
        ## Naive Bayes
        # http://scikit-learn.org/stable/modules/naive_bayes.html
        self.multinomial_nb = (
            "Naive Bayes classifier for multinomial models"
            , sklearn.naive_bayes.MultinomialNB())
        self.bernoulli_nb = (
            "Naive Bayes classifier for multivariate Bernoulli models"
            , sklearn.naive_bayes.BernoulliNB())
        pass

    def _init_ensemble_methods(self):
        ## Ensemble methods
        # http://scikit-learn.org/stable/modules/ensemble.html
        self.random_forest_classifier = (
            "random forest classifier",
            sklearn.ensemble.RandomForestClassifier(
                max_depth=5
                , n_estimators=10
                , max_features=1
                , n_jobs=-1
                , random_state=32414343))
        self.ada_boost_classifier = (
            "Ada boost classifier",
            sklearn.ensemble.AdaBoostClassifier(random_state=67294))
        pass

    def _init_neighbor_methods(self):
        ## Neighbour methods
        # http://scikit-learn.org/stable/modules/neighbors.html
        self.k_neighors_classifier= (
            "K nearest keighbours"
            , sklearn.neighbors.KNeighborsClassifier())
        pass
