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
        "name": "pluto",
        "description": "Neil sucks",
        "position" : 9
    }
    
