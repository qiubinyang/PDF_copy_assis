from aip import AipOcr

def OCR(filename):
    APP_ID = '16463605'
    API_KEY = 'PRne71jK8wGyZpRFiEAubbsI'
    SECRET_KEY = 'RZXStga5htglPvHfpD2HZcKAC0uuI3PW'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    img = get_file_content(filename)
    result = client.basicGeneral(img)

    ocr_result = ""
    for i in result['words_result']:
        ocr_result += i['words']+'\n'
    # print(ocr_result)
    return ocr_result