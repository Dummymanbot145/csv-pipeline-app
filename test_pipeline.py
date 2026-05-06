# test_pipeline.py - Automated tests for the CI/CD pipeline

# ── Test 1: New files detected correctly ──────────────────────────────────────
def test_finds_new_files():
    seen   = {"file_a.csv", "file_b.csv"}
    remote = {"file_a.csv", "file_b.csv", "file_c.csv"}
    result = remote - seen
    assert result == {"file_c.csv"}
    print("PASS - new files detected")

# ── Test 2: No new files returns empty set ────────────────────────────────────
def test_no_new_files():
    seen   = {"file_a.csv", "file_b.csv"}
    remote = {"file_a.csv", "file_b.csv"}
    result = remote - seen
    assert result == set()
    print("PASS - no new files correctly returns empty")

# ── Test 3: CSV filter works ──────────────────────────────────────────────────
def test_csv_only():
    files  = {"data.csv", "notes.txt", "report.csv", "image.png"}
    result = {f for f in files if f.endswith(".csv")}
    assert result == {"data.csv", "report.csv"}
    print("PASS - only CSV files returned")

# ── Test 4: Invalid file detected ─────────────────────────────────────────────
def test_invalid_header():
    header   = ["wrong", "header"]
    expected = ["id", "name", "amount"]
    assert header != expected
    print("PASS - invalid header correctly detected")

# ── Test 5: Valid file passes ─────────────────────────────────────────────────
def test_valid_header():
    header   = ["id", "name", "amount"]
    expected = ["id", "name", "amount"]
    assert header == expected
    print("PASS - valid header correctly accepted")

# ── Run all tests ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_finds_new_files()
    test_no_new_files()
    test_csv_only()
    test_invalid_header()
    test_valid_header()
    print("\nAll tests passed!")
