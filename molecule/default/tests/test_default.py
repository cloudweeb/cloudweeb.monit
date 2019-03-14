import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_packages(host):
    p = host.package("monit")
    assert p.is_installed


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:2812")
    assert s.is_listening
