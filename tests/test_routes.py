def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/solar_system/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_specific_planet_that_exists(client, two_saved_planets):
    # Act
    response = client.get("/solar_system/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "Neil sucks",
        "position" : 9
    }

def test_get_specific_planet_that_does_not_exist(client):
    # Act
    response = client.get("/solar_system/planets/1")
    
    # Assert
    assert response.status_code == 404

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/solar_system/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Pluto",
        "description": "Neil sucks",
        "position" : 9
        },
        {
        "id": 2,
        "name": "Venus",
        "description": "She's got it",
        "position" : 3
        }
    ]   

def test_create_new_planet(client):
    # Act
    response = client.post("/solar_system/planets", 
        json={
        "name" : "Earth",
        "description" : "tiny blue marble",
        "position" : 3
        }
        )
    response_text = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_text == "Planet Earth successfully created"

    