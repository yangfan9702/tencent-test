from typing import List, Dict
from datetime import date


def make_response(d: List[Dict]) -> List:
    for _ in d:
        for k, v in _.items():
            if type(v) is date:
                _[k] = v.strftime('%Y-%m-%d')
    return d
