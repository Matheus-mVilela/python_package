import datetime

def matheus(request):
    pc = [
        {
            "_id": "4279659b-6f57-41de-9dc2-e075a75e2661",
            "company_owner": 2,
            "strategies": [],
            "services": [
                {
                    "id": "82d876ce-2f29-418b-8e38-da0171e2ad62",
                    "line_id": "4279659b-6f57-41de-9dc2-e075a75e2661",
                    "strategies": [],
                    "departures": [
                        {
                            "id": "bc434663-aabd-48ec-b001-1edd5e0672e2",
                            "line_id": "4279659b-6f57-41de-9dc2-e075a75e2661",
                            "service_id": "82d876ce-2f29-418b-8e38-da0171e2ad62",
                            "strategies": [
                                {
                                    "algorithm": {
                                        "algorithm_id": 1,
                                        "name": "testeciclosdashboards",
                                    },
                                    "weekdays": [-1],
                                    "agencies": [
                                        {"value": 2696, "label": "TODOS"}
                                    ],
                                    "validity": {"start": "", "end": "",},
                                    "created_at": datetime.datetime(
                                        2022, 8, 18, 10, 40, 6
                                    ),
                                }
                            ],
                            "active": True,
                        }
                    ],
                    "active": True,
                },
            ],
            "active": True,
        }
    ]
    create_travels_process_pricings(
        pricings_configs=pc, validate_type='mongodb'
    )
