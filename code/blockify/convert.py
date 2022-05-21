import base64, gzip

class ExternalHelper:
    def encodeJSONToCodeTemplate(self, code):
        return base64.b64encode(gzip.decompress()).decode()