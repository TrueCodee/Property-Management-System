class MaintenanceRequest:
    requests = []

    def __init__(self, request_id, tenant_id, property_id, description, status, date_submitted):
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.property_id = property_id
        self.description = description
        self.status = status
        self.date_submitted = date_submitted

    @classmethod
    def submit_request(cls, request):
        cls.requests.append(request)
        print(f"Maintenance request {request.request_id} submitted.")

    @classmethod
    def track_request_status(cls, request_id):
        for request in cls.requests:
            if request.request_id == request_id:
                print(f"Request status: {request.status}")
                return
        print("Request not found!")

    @classmethod
    def view_requests(cls):
        for request in cls.requests:
            print(f"ID: {request.request_id}, Tenant ID: {request.tenant_id}, Property ID: {request.property_id}, Description: {request.description}, Status: {request.status}, Date: {request.date_submitted}")

 # Input
request1 = MaintenanceRequest(
    "R001", "T001", "P001", "Leaky faucet", "Pending", "2024-07-25")
MaintenanceRequest.submit_request(request1)
MaintenanceRequest.view_requests()

MaintenanceRequest.track_request_status("R001")
