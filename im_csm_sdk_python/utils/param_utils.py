from urllib.parse import quote as q_parse


def sort_params(params: dict) -> dict:
    """Sort dictionary parameters by key.

    Args:
        params (dict): Dictionary of parameters to sort.

    Returns:
        dict: Sorted dictionary by keys
    """
    return {key: params[key] for key in sorted(params.keys())}


def to_str(param: bool | str) -> str:
    """Convert parameter to string.

    Args:
        param (bool or str): The parameter to convert

    Returns:
        str: The converted parameter
    """
    if isinstance(param, bool):
        return q_parse(str(param).lower())
    return q_parse(str(param))
