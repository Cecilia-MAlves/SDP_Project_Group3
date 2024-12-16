def test_cpu_temp(mocker, client):
    # Mock the CPUTemperature class
    mock_cpu = mocker.patch('app.routes.read_cpu_temperature')
    mock_cpu.return_value = 45.0

    response = client.get('/cpu/temp') 
    assert response.status_code == 200
    assert response.json == {"Temperature (C)": 45.0}


def test_cpu_temp_status_fine(mocker, client):
    # Mock the CPUTemperature class
    mock_cpu = mocker.patch('app.routes.read_cpu_temperature')
    mock_cpu.return_value = 45.0

    response = client.get('/cpu/temp/error') 
    assert response.status_code == 200
    assert response.json == {"Temperature (C)": 45.0}
    assert response.json == {"Status": "fine"}


def test_cpu_temp_status_hot(mocker, client):
    # Mock the CPUTemperature class
    mock_cpu = mocker.patch('app.routes.read_cpu_temperature')
    mock_cpu.return_value = 65.0

    response = client.get('/cpu/temp/error') 
    assert response.status_code == 200
    assert response.json == {"Temperature (C)": 65.0}
    assert response.json == {"Status": "too hot"}

def test_disk_usage(mocker, client):
    # Mock the shutil.disk_usage function
    mock_disk = mocker.patch('app.routes.shutil.disk_usage')
    mock_disk.return_value = (100, 50, 50)  # Total, used, free

    response = client.get('/disk/usage')  
    assert response.status_code == 200
    assert response.json == {"Disk Usage (%)": 50.0}
