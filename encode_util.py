# -*- coding:utf-8 -*-

def decode_list(data,encoding='utf-8'):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode(encoding)
        elif isinstance(item, list):
            item = decode_list(item,encoding)
        elif isinstance(item, dict):
            item = decode_dict(item, encoding)
        rv.append(item)
    return rv

def decode_dict(data, encoding='utf-8'):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode(encoding)
        if isinstance(value, unicode):
            print value
            value = value.encode(encoding)
        if isinstance(value, list):
            value = decode_list(value, encoding)
        if isinstance(value, dict):
            value = decode_dict(value, encoding)
        print key, value
        rv[key] = value
    return rv
