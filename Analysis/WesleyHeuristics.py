import logging
import numpy as np


def estimate_mocking(text) -> list:
    """Heuristic for detecting mocking statements in social media documents"""
    document = ''
    if isinstance(text, list):
        for word in text:
            document = document + word + ' '
    elif isinstance(text, str):
        document = text
    else:
        logging.error('Expected a list or string for function estimate_mocking, instead received' + str(type(text)))
        return []

    mock_score = []
    length = len(document)
    upperlist = np.array(list(map(int, list(map(str.isupper, document)))), dtype=np.int8)
    diff = np.abs(np.diff(upperlist))
    nonzero = np.nonzero(diff)


