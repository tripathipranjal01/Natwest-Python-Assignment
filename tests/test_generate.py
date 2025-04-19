import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_generate_report():
    from app.services.processor import generate_report
    result = generate_report()
    assert "output.csv" in result
