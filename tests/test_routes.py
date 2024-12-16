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


def test_memory_usage(mocker, client):
    """
    If routes.py has 'import psutil' and calls psutil.virtual_memory()
    """
    mock_memory = mocker.patch('app.routes.psutil.virtual_memory')
    MockMemory = namedtuple('MockMemory', ['percent'])
    mock_memory.return_value = MockMemory(percent=30.0)

    response = client.get('/memory/usage')
    assert response.status_code == 200
    assert response.json == {"Memory Usage (%)": 30.0}


def test_network_stats(mocker, client):
    """
    If routes.py has 'import psutil' and calls psutil.net_io_counters()
    """
    mock_net = mocker.patch('app.routes.psutil.net_io_counters')
    MockNetIO = namedtuple('MockNetIO', ['bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv'])
    mock_net.return_value = MockNetIO(123456, 654321, 100, 200)

    response = client.get('/network/stats')
    assert response.status_code == 200
    assert response.json == {
        "Bytes Sent": 123456,
        "Bytes Received": 654321,
        "Packets Sent": 100,
        "Packets Received": 200
    }


def test_system_uptime(mocker, client):
    """
    If routes.py has 'import psutil' and calls psutil.boot_time()
    """
    mock_boot_time = mocker.patch('app.routes.psutil.boot_time')
    mock_current_time = mocker.patch('time.time')

    mock_boot_time.return_value = 1_600_000_000
    mock_current_time.return_value = 1_600_000_100  # 100s after boot

    response = client.get('/system/uptime')
    assert response.status_code == 200
    assert response.json == {"Uptime (s)": 100}
