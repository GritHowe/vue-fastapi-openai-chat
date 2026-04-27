def success_response(data):
    return {"code": 200, "msg": "success", "data": data}

def error_response(msg):
    return {"code": 500, "msg": msg, "data": None}