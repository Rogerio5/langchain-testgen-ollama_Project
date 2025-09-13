from datetime import datetime

def dias_entre_datas(data1_str, data2_str):
    formato = "%Y-%m-%d"
    data1 = datetime.strptime(data1_str, formato)
    data2 = datetime.strptime(data2_str, formato)
    return abs((data2 - data1).days)
