
from phonemizer.phonemize import phonemize
from phonemizer.separator import Separator
def phonemize_punjabi(text):
    """ 
    Return a phonemized version of the given text.
    
    Parameters
    ----------

    text (str): The text to be phonemized.

    Returns
    -------

    phones(list): List of hi phonemes for the given text.
    """
    seperators = Separator(word="@", phone=" ")
    phones = phonemize(
        text,
        separator=seperators,
        backend="espeak",
        language="pa",
        language_switch="remove-flags",
        with_stress=True,
    )
    phones = phones.replace("@", " | ").strip()
#    phones = phones.split(" ")


    return phones



