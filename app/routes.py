from flask import request, Blueprint, make_response
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/solar_system")

@planets_bp.route("/planets", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    position_from_sun=request_body["position_from_sun"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# @planets_bp.route("/planets", methods=["GET"])
# def endpoint_name():
#     response_body = {
#     "id": "?????",
#     "name": "Pluto",
#     "description": "The best planet, despite Neil.",
#     "position_from_sun": 9
#     }
#     return response_body



# Create the following endpoints, with similar functionality presented in the Hello Books API:
# As a client, I want to send a request with new valid planet data and get a success response, so that I know the API saved the planet data
# As a client, I want to send a request to get all existing planets, so that I can see a list of planets, with their id, name, description, and other data of the planet.
# As a client, I want to send a request to get one existing planet, so that I can see the id, name, description, and other data of the planet.