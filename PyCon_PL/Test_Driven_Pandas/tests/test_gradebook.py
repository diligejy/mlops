import pandas as pd 

def test_results_are_grouped_by_student_group():
    students = [{
        "ID" : 1,
        "Name" : "Doe, John",
        "NetID" : "JXD12345",
        "Email Address" : "JOHN.DOE@EXAMPLE.EDU",
        "Group" : 1,
    }]
    students_df = pd.DataFrame(data=students).set_index("ID")
    
    result = {}
    assert list(result.keys()) == [1]