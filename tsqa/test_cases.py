'''
Some base test cases that do environment handling for you
'''

import tsqa.endpoint
import tsqa.environment
import tsqa.utils
unittest = tsqa.utils.import_unittest()

import os

class EnvironmentCase(unittest.TestCase):
    '''
    This class will get an environment (which is unique) but won't start it
    '''

    @classmethod
    def setUpClass(cls):
        # call parent constructor
        super(EnvironmentCase, cls).setUpClass()

        SOURCE_DIR = '/home/thjackso/src/trafficserver'
        TMP_DIR = '/home/thjackso/src/tsqa/tmp'
        ef = tsqa.environment.EnvironmentFactory(SOURCE_DIR, os.path.join(TMP_DIR, 'base_envs'))
        cls.environment = ef.get_environment()


class DynamicHTTPEndpointCase(unittest.TestCase):
    '''
    This class will set up a dynamic http endpoint that is local to this class
    '''
    @classmethod
    def setUpClass(cls):
        # call parent constructor
        super(DynamicHTTPEndpointCase, cls).setUpClass()

        cls.http_endpoint = tsqa.endpoint.DynamicHTTPEndpoint()
        cls.http_endpoint.start()

        cls.http_endpoint.ready.wait()

        # create local requester object
        cls.track_requests = tsqa.endpoint.TrackingRequests(cls.http_endpoint)

    def endpoint_url(self, path=''):
        '''
        Get the url for the local dynamic endpoint given a path
        '''
        return 'http://127.0.0.1:{0}{1}'.format(self.http_endpoint.address[1],
                                                path)
