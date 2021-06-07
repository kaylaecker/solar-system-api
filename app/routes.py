from flask import request, Blueprint, make_response, jsonify
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/solar_system")

@planets_bp.route("/planets", strict_slashes=False, methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "position": planet.position_from_sun
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        position_from_sun=request_body["position"])

        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/planets/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return make_response(f"Planet {planet_id} not found", 404)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "position": planet.position_from_sun
        }
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"],
        planet.description = form_data["description"]
        planet.position_from_sun = form_data["position"]

        db.session.commit()
        return make_response(f"Planet {planet_id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet {planet_id} successfully deleted")
