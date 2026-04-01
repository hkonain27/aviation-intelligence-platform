from flask import Blueprint, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/api/dashboard-data", methods=["GET"])
def get_dashboard_data():
    return jsonify({
        "summaryCards": [
            {"title": "Flights Analyzed", "value": "184,230", "change": "+12.4%", "icon": "Plane"},
            {"title": "Avg Delay", "value": "18 min", "change": "-3.2%", "icon": "Clock3"},
            {"title": "High-Risk Weather Days", "value": "47", "change": "+6.8%", "icon": "CloudRain"},
            {"title": "Prediction Accuracy", "value": "66.0%", "change": "+1.1%", "icon": "TrendingUp"},
        ],
        "monthlyDelayData": [
            {"month": "Jan", "avgDelay": 22, "predicted": 20},
            {"month": "Feb", "avgDelay": 19, "predicted": 18},
            {"month": "Mar", "avgDelay": 25, "predicted": 23},
            {"month": "Apr", "avgDelay": 17, "predicted": 16},
            {"month": "May", "avgDelay": 15, "predicted": 14},
            {"month": "Jun", "avgDelay": 24, "predicted": 21},
            {"month": "Jul", "avgDelay": 29, "predicted": 26},
            {"month": "Aug", "avgDelay": 21, "predicted": 20},
            {"month": "Sep", "avgDelay": 16, "predicted": 15},
            {"month": "Oct", "avgDelay": 14, "predicted": 13},
            {"month": "Nov", "avgDelay": 20, "predicted": 18},
            {"month": "Dec", "avgDelay": 31, "predicted": 28},
        ],
        "airportRiskData": [
            {"airport": "ATL", "risk": 84},
            {"airport": "CLT", "risk": 73},
            {"airport": "JFK", "risk": 79},
            {"airport": "ORD", "risk": 88},
            {"airport": "DFW", "risk": 68},
            {"airport": "LAX", "risk": 55},
        ],
        "causeBreakdown": [
            {"name": "Weather", "value": 34},
            {"name": "Carrier", "value": 26},
            {"name": "NAS", "value": 18},
            {"name": "Late Aircraft", "value": 15},
            {"name": "Security", "value": 7},
        ],
        "forecastData": [
            {"day": "Mon", "actual": 14, "predicted": 17},
            {"day": "Tue", "actual": 19, "predicted": 22},
            {"day": "Wed", "actual": 12, "predicted": 13},
            {"day": "Thu", "actual": 21, "predicted": 25},
            {"day": "Fri", "actual": 28, "predicted": 31},
            {"day": "Sat", "actual": 26, "predicted": 29},
            {"day": "Sun", "actual": 18, "predicted": 21},
        ],
        "mockFlights": [
            {"id": "AA102", "route": "CLT → JFK", "airport": "CLT", "airline": "American", "weather": "Rain", "predictedDelay": 42, "status": "High Risk", "confidence": 91},
            {"id": "DL248", "route": "ATL → ORD", "airport": "ATL", "airline": "Delta", "weather": "Storm", "predictedDelay": 58, "status": "Critical", "confidence": 94},
            {"id": "UA771", "route": "EWR → LAX", "airport": "EWR", "airline": "United", "weather": "Clear", "predictedDelay": 9, "status": "Low Risk", "confidence": 82},
            {"id": "WN503", "route": "DAL → HOU", "airport": "DAL", "airline": "Southwest", "weather": "Wind", "predictedDelay": 27, "status": "Moderate", "confidence": 86},
            {"id": "B6291", "route": "JFK → MCO", "airport": "JFK", "airline": "JetBlue", "weather": "Snow", "predictedDelay": 49, "status": "High Risk", "confidence": 90},
        ],
    })
