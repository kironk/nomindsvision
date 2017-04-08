import logging

import requests

from coredata import QuandlException

log = logging.getLogger('main')


class NSE:
    """
    
    """
    def __init__(self, quandl_api_key):
        """
        
        :param quandl_api_key: 
        """
        self.quandl_api_key = quandl_api_key

        quandl_nse_url = f'https://www.quandl.com/api/v3/datasets.json?' \
                         f'api_key={self.quandl_api_key}&database_code=NSE&' \
                         f'sort_by=id'

        log.debug('Downloading NSE data sets from Quandl.')
        log.debug(f'URL: {quandl_nse_url}.')

        response = requests.get(quandl_nse_url)
        if response.status_code != 200:
            raise QuandlException(response.text)

        response_json = response.json()
        data_sets = response_json['datasets']
        data_sets_total_pages = response_json['meta']['total_pages']

        log.debug(f'Downloaded data set 01/{data_sets_total_pages}.')

        for page in range(2, data_sets_total_pages + 1):
            response = requests.get(quandl_nse_url + f'&page={page}')
            log.debug(f'Downloaded data set {page:02}/{data_sets_total_pages}.')

            response_json = response.json()
            data_sets += response_json['datasets']
        else:
            log.debug('Downloading complete.')

        data_sets = sorted(data_sets,
                           key=lambda data_set: data_set['dataset_code'])
        self.scrips = {data_set['dataset_code']: data_set for data_set in
                       data_sets}

    def __str__(self):
        """
        
        :return: 
        """
        return ', '.join([scrip for scrip in self.scrips])

    def __repr__(self):
        """
        
        :return: 
        """
        return f'{self.__class__.__name__}(\'{self.quandl_api_key}\')'

    def get_name(self, scrip):
        """
        
        :param scrip: 
        :return: 
        """
        return self.scrips.get(scrip, {}).get('name', 'Data not available')
