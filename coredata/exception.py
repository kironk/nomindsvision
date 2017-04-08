import json


class QuandlException(Exception):
    """
    
    """

    def __init__(self, quandl_response_text):
        """
        
        :param quandl_response_text: 
        """
        quandl_response_text = json.loads(quandl_response_text)
        self.error_code = quandl_response_text['quandl_error']['code']
        self.error_message = quandl_response_text['quandl_error']['message']

    def __str__(self):
        """
        
        :return: 
        """
        return f'[Error Code: {self.error_code}] {self.error_message}'
