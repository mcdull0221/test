
class GlobalVar:
    Id = '0'
    url = '2'
    run = '3'
    request_way = '4'
    cookie = '5'
    header = '6'
    case_depend = '8'
    data_depend = '10'
    field_depend = '9'
    data = '11'
    expect = '12'
    result = '13'


# 获取caseid
def get_id():
    return GlobalVar.Id


# 获取url
def get_url():
    return GlobalVar.url


# 是否运行
def get_run():
    return GlobalVar.run


# 获取运行方式
def get_request_way():
    return GlobalVar.request_way


# 获取header
def get_header():
    return GlobalVar.header


# 获取case_depend
def get_case_depend():
    return GlobalVar.case_depend


# 获取data_depend
def get_data_depend():
    return GlobalVar.data_depend


# 获取field_depend
def get_field_depend():
    return GlobalVar.field_depend


# 获取field_depend
def get_data():
    return GlobalVar.data


# 获取field_depend
def get_expect():
    return GlobalVar.expect


# 获取field_depend
def get_result():
    return GlobalVar.result
