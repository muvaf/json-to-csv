def flatten_json(nested_json, separator='_', prefix=''):
     """
     Flatten a nested JSON object into a single level dictionary.

     Args:
         nested_json (dict/list): The nested JSON object or array to flatten
         separator (str): Separator to use between nested keys
         prefix (str): Prefix for the current key (used in recursion)

     Returns:
         dict: Flattened dictionary with compound keys
     """
     flattened = {}

     # Handle dictionary
     if isinstance(nested_json, dict):
         for key, value in nested_json.items():
             new_key = f"{prefix}{separator}{key}" if prefix else key

             if isinstance(value, (dict, list)):
                 flattened.update(flatten_json(value, separator, new_key))
             else:
                 flattened[new_key] = value

     # Handle list
     elif isinstance(nested_json, list):
         for i, value in enumerate(nested_json):
             new_key = f"{prefix}{separator}{i}" if prefix else str(i)

             if isinstance(value, (dict, list)):
                 flattened.update(flatten_json(value, separator, new_key))
             else:
                 flattened[new_key] = value

     return flattened
