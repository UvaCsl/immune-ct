import os
import pickle


def save_as_pickle(var, filepath):
    """Save var as pickle given filepath"""
    create_dirpath_if_not_exists(filepath)
    with open(filepath, 'wb') as f:
        pickle.dump(var, f)


def load_pickle(filepath):
    """Load pickle in the given filepath"""
    with open(filepath, 'rb') as f:
        return pickle.load(f)
    
def create_dirpath_if_not_exists(filepath):
    """Create directory path given filepath if it does not exists"""
    # Get directory path
    dirpath = os.path.dirname(filepath)

    # Create path if it does not exists
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)