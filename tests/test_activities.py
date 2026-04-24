def test_get_activities_returns_activity_data_and_cache_headers(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Basketball" in response.json()
    assert response.headers["cache-control"] == "no-store"
    assert response.headers["pragma"] == "no-cache"
