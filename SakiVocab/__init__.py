# In SakiVocab/__init__.py

from .Goodbye import load_goodbye_data
from .GreetingsData import load_greetings_data
from .JPFLore import load_jpflore_data
from .Common import load_common_data


# Define a function to load all vocab files if needed
def load_all_vocab_files():
    vocab_data = {}
    vocab_data.update(load_goodbye_data())
    vocab_data.update(load_greetings_data())
    vocab_data.update(load_jpflore_data())
    vocab_data.update(load_common_data())
    # Add more updates for other vocab files if needed
    return vocab_data
