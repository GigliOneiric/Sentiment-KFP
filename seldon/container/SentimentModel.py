import numpy as np
import keras
import logging
import pickle

class SentimentModel(object):
    def __init__(self):
        self.loaded = False

    def load(self):
        try:
            with open('/mnt/model.pickle', 'rb') as file:
                self.model = pickle.load(file)
            self.model.make_predict_function()
            self.loaded = True
            logging.warning("model loaded")
        except (AttributeError,  EOFError, ImportError, IndexError) as e:
            # secondary errors
            logging.warning(traceback.format_exc(e))
        except Exception as e:
            # everything else, possibly fatal
            logging.warning(traceback.format_exc(e))
            return

    def predict(self, X, feature_names):
        if not self.loaded:
            self.load()
        logging.warning(X)
        sentiment = self.model.predict(np.array([X]))
        logging.warning(sentiment)
        return sentiment
