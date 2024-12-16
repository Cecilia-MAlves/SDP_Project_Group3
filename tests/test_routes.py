def test_cpu_temp(mocker, client):
    # Mock the CPUTemperature class
    mock_cpu = mocker.patch('app.routes.read_cpu_temperature')
    mock_cpu.return_value = 45.0

    response = client.get('/cpu/temp')  # Ensure the route matches your app
    assert response.status_code == 200
    assert response.json == {"Temperature (C)": 45.0}


def test_disk_usage(mocker, client):
    # Mock the shutil.disk_usage function
    mock_disk = mocker.patch('app.routes.shutil.disk_usage')
    mock_disk.return_value = (100, 50, 50)  # Total, used, free

    response = client.get('/disk/usage')  # Ensure the route matches your app
    assert response.status_code == 200
    assert response.json == {"Disk Usage (%)": 50.0}

def test_memory_usage(self, mocker, client):
        # Mock a memory usage function
        mock_memory = mocker.patch('app.routes.psutil.virtual_memory')
        mock_memory.return_value = mocker.Mock(percent=70)

        response = client.get('/memory/usage')  # Ensure the route matches your app
        assert response.status_code == 200
        assert response.json == {"Memory Usage (%)": 70.0}

    def test_network_stats(self, mocker, client):
        # Mock a network stats function
        mock_network = mocker.patch('app.routes.psutil.net_io_counters')
        mock_network.return_value = mocker.Mock(bytes_sent=1024, bytes_recv=2048)

        response = client.get('/network/stats')  # Ensure the route matches your app
        assert response.status_code == 200
        assert response.json == {
            "Bytes Sent": 1024,
            "Bytes Received": 2048
        }

    def test_system_uptime(self, mocker, client):
        # Mock a system uptime function
        mock_uptime = mocker.patch('app.routes.time.time')
        mock_uptime.return_value = 100000

        response = client.get('/system/uptime')  # Ensure the route matches your app
        assert response.status_code == 200
        assert response.json == {"Uptime (seconds)": 100000}
