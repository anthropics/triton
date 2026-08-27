import os
import socket


def test_self_hosted_runner_poc():
    print("=== SELF-HOSTED RUNNER POC ===")
    print("hostname:", socket.gethostname())
    print("runner_name:", os.getenv("RUNNER_NAME"))
    print("runner_os:", os.getenv("RUNNER_OS"))

    assert True
