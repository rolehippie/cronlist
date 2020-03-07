import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_script_file(host):
    file = host.file("/usr/bin/cronlist")
    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o775

