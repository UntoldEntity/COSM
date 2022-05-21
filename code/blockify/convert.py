import base64, gzip, asyncio, websockets

class ExternalHelper:
    def encodeJSONToCodeTemplate(self, code):
        return base64.b64encode(gzip.decompress(code)).decode()
    
    def SendItemToCodeUtilitiesItemAPI(self, json):
        pass