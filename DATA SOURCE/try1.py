import json

festival_data = {
    "Ganesh Chaturthi": {
        "date_range": [("2022-08-31", "2022-09-09")],
        "affected_areas": ["Girgaon", "Dadar", "Lalbaug", "Byculla"],
        "traffic_increase": 1.5,
        "pedestrian_increase": 2.0
    },
    "Navratri": {
        "date_range": [("2022-09-26", "2022-10-04")],
        "affected_areas": ["Girgaon", "Vile Parle", "Ghatkopar"],
        "traffic_increase": 1.3,
        "pedestrian_increase": 1.5
    },
    "Diwali": {
        "date_range": [("2022-10-24", "2022-10-30")],
        "affected_areas": ["Crawford Market", "Dadar", "Bandra"],
        "traffic_increase": 1.4,
        "pedestrian_increase": 1.6
    },
    "Eid-ul-Fitr": {
        "date_range": [("2022-05-03", "2022-05-04")],
        "affected_areas": ["Mohammad Ali Road", "Bandra", "Kurla"],
        "traffic_increase": 1.4,
        "pedestrian_increase": 1.8
    },
    "Christmas": {
        "date_range": [("2022-12-25", "2022-12-25")],
        "affected_areas": ["Bandra", "Malad", "Colaba"],
        "traffic_increase": 1.2,
        "pedestrian_increase": 1.5
    },
    "New Year's Eve": {
        "date_range": [("2022-12-31", "2022-12-31")],
        "affected_areas": ["Marine Drive", "Bandra", "Juhu"],
        "traffic_increase": 2.0,
        "pedestrian_increase": 2.5
    },
    "Makar Sankranti": {
        "date_range": [("2022-01-14", "2022-01-14")],
        "affected_areas": ["Juhu", "Marine Drive"],
        "traffic_increase": 1.3,
        "pedestrian_increase": 1.5
    },
    "Holi": {
        "date_range": [("2022-03-18", "2022-03-18")],
        "affected_areas": ["Residential Areas"],
        "traffic_increase": 1.2,
        "pedestrian_increase": 1.7
    },
    "Dussehra": {
        "date_range": [("2022-10-05", "2022-10-05")],
        "affected_areas": ["Shivaji Park", "Girgaon", "Borivali"],
        "traffic_increase": 1.5,
        "pedestrian_increase": 2.0
    },
    "Muharram": {
        "date_range": [("2022-08-08", "2022-08-08")],
        "affected_areas": ["Byculla", "Dongri"],
        "traffic_increase": 1.5,
        "pedestrian_increase": 1.8
    },
    "Gudi Padwa": {
        "date_range": [("2022-04-02", "2022-04-02")],
        "affected_areas": ["Dadar"],
        "traffic_increase": 1.3,
        "pedestrian_increase": 1.5
    }
}

# Save festival_data to JSON file
with open('festival_data.json', 'w') as f:
    json.dump(festival_data, f, indent=4)

print("Festival data saved to festival_data.json")