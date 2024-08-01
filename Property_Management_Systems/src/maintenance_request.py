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
