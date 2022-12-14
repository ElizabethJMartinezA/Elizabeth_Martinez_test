from Eli_SN_Version_Compare import function 

def test_comp1():
    assert function.versionComparisson("9.98.1", "9.9") == "Version 9.98.1 is greater than version 9.9"
def test_comp12():
    assert function.versionComparisson("0.9.1","8.0.1") == "Version 0.9.1 is lesser than version 8.0.1"
def test_comp3():
    assert function.versionComparisson("0", "0.0.0") == "Version 0 is equal than version 0.0.0"
def test_comp4():
    assert function.versionComparisson("1.2.3.4.1", "1") == "Version 1.2.3.4.1 is greater than version 1"