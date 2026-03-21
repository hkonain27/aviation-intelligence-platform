from flask import Blueprint, request, jsonify

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No input data provided"
        }), 400

    required_fields = ["airline", "origin", "destination", "hour", "day_of_week", "month"]

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "status": "error",
            "message": f"Missing required fields: {', '.join(missing_fields)}"
        }), 400

    try:
        airline = str(data["airline"])
        origin = str(data["origin"])
        destination = str(data["destination"])
        hour = int(data["hour"])
        day_of_week = int(data["day_of_week"])
        month = int(data["month"])
    except (ValueError, TypeError):
        return jsonify({
            "status": "error",
            "message": "Invalid data types provided"
        }), 400

    # Dummy prediction logic for now
    # Replace this later with real model prediction
    if hour >= 15:
        prediction = "Delay Likely"
        delay_probability = 0.72
    else:
        prediction = "On Time Likely"
        delay_probability = 0.28

    return jsonify({
        "status": "success",
        "input": {
            "airline": airline,
            "origin": origin,
            "destination": destination,
            "hour": hour,
            "day_of_week": day_of_week,
            "month": month
        },
        "prediction": prediction,
        "delay_probability": delay_probability
    }), 200