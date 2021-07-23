# class JsosError(Exception):
#     def __ini__(self, msg):
#         self.msg = msg

def python_to_json(obj):
    if isinstance(obj, int) or isinstance(obj, float):
        return str(obj)
    elif isinstance(obj, bool):
        result = str(obj)
        result = result.replace("F", "f")
        result = result.replace("T", "t")
        return result
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif obj is None:
        result = str(obj).replace("None", "null")
        return result
    elif isinstance(obj, tuple) or isinstance(obj, list):
        result = "["
        pos = 0
        for val in obj:
            result += f"{python_to_json(val)}"
            if pos != len(obj) - 1:
                result += ", "
            pos += 1
        result += "]"
        return result
    elif isinstance(obj, dict):
        result = "{"
        pos = 0
        for key, val in obj.items():
            result += F'"{key}": {python_to_json(val)}'
            if pos != len(obj) - 1:
                result += ", "
            pos += 1
        result += "}"
        return result
    else:
        result = str(vars(obj)).replace("'", '"')
        result = result.replace("(", "[")
        result = result.replace(")", "]")
        return result
    raise TypeError

def json_to_python(result):
    result = result.replace("true", "True")
    result = result.replace("false", "False")
    result = result.replace("null", "None")
    return eval(result)

