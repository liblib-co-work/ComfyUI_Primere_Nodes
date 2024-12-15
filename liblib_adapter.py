def get_field_key_by_value(mappings, value: str):
    """根据value查询field对应的key"""
    for k, v in mappings.items():
        if v == value:
            return k
    return ''
