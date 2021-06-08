def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/solar_system/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_with_records(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
        },
        {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
        } 
    ]   
