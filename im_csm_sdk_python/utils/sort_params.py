def sort_params(params):
    """Sort dictionary parameters by key.

    Args:
        params (dict): Dictionary of parameters to sort.

    Returns:
        dict: Sorted dictionary by keys
    """
    return {key: params[key] for key in sorted(params.keys())} 