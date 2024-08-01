import unittest
from maintenance_request import MaintenanceRequest
from io import StringIO
import sys


class TestMaintenanceRequest(unittest.TestCase):

    def setUp(self):
        MaintenanceRequest.requests.clear()

    def test_submit_request(self):
        print("Running test_submit_request...")
        request = MaintenanceRequest(
            "R002", "T002", "P002", "Broken window", "Pending", "2024-08-01")
        MaintenanceRequest.submit_request(request)
        self.assertIn(request, MaintenanceRequest.requests)
        print(
            f"Maintenance request {request.request_id} submitted for {request.description}.")

    def test_track_request_status(self):
        print("Running test_track_request_status...")
        request = MaintenanceRequest(
            "R003", "T003", "P003", "Clogged drain", "Pending", "2024-09-01")
        MaintenanceRequest.submit_request(request)

        captured_output = StringIO()
        sys.stdout = captured_output
        MaintenanceRequest.track_request_status("R003")
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        self.assertIn("Request status: Pending", output)
        print(f"Request status tracked: {output}")


if __name__ == '__main__':
    unittest.main()
