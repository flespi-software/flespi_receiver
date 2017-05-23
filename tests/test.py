# -*- coding: utf-8 -*-

from context import flespi_receiver

import unittest

api_key = 'gr5jkmFPqhN9MVJ6sCGlkz1xzurPUg0ZxV8F5DllIWiiFSeXiJ7s8WNvg49Z8ZOv'
channel_id = 11
timeout = 10
delete_flag = True
start_key = 0


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_read_from_flespi(self):
        receiver = flespi_receiver.flespi_receiver()
        receiver.configure(channel_id, api_key, timeout, delete_flag)
        receiver.target_url = "http://localhost:9004/gw/channels/" + \
            str(channel_id) + '/messages'
        print(receiver.target_url)

        stdout_handler1 = flespi_receiver.stdout_handler_class(stdout=1)
        receiver.add_handler(stdout_handler1)

        #wialon_handler = flespi_receiver.wialon_retranslator_handler_class(
        #    host='localhost', port=12374)  # specify listening host:port
        #receiver.add_handler(wialon_handler)

        receiver.start()


if __name__ == '__main__':
    unittest.main()
