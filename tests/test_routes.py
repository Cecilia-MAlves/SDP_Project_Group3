def test_cpu_temp(mocker, client):
    # Mock the CPUTemperature class
    mock_cpu = mocker.patch('app.routes.read_cpu_temperature')
    mock_cpu.return_value = 45.0

    response = client.get('/cpu/temp')  # Ensure the route matches your app
    assert response.status_code == 200
    assert response.json == {"temp": 45.0}


def test_disk_usage(mocker, client):
    # Mock the shutil.disk_usage function
    mock_disk = mocker.patch('app.routes.shutil.disk_usage')
    mock_disk.return_value = (100, 50, 50)  # Total, used, free

    response = client.get('/disk/usage')  # Ensure the route matches your app
    assert response.status_code == 200
    assert response.json == {"disk_usage_percent": 50.0}