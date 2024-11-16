import subprocess

def test_cli_correct_usage(capsys):
    """Tests that dividing by zero results in a non-zero exit code and error message."""
    result = subprocess.run(['python', 'main.py', '5', '/', '0'], capture_output=True, text=True)
    assert result.returncode != 0  # Check for non-zero exit code (error)
    assert "ZeroDivisionError" in result.stderr  # Verify error message in stderr
