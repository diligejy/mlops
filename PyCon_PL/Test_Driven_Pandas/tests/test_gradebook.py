import pandas as pd 
from typing import cast

def generate_gradebook(students_df:pd.DataFrame) -> dict[int, pd.DataFrame]:
    return {
        cast(int, group): pd.DataFrame()
        for group, table in students_df.groupby("Group")
    }
    
def test_results_are_grouped_by_student_group():
    students = [{
        "ID" : 1,
        "Name" : "Doe, John",
        "NetID" : "JXD12345",
        "Email Address" : "JOHN.DOE@EXAMPLE.EDU",
        "Group" : 1,
    }]
    students_df = pd.DataFrame(data=students).set_index("ID")
    
    result = generate_gradebook(students_df=students_df)
    assert list(result.keys()) == [1]
    
def test_results_are_grouped_by_student_group_for_students_in_multiple_group():
    students = [{
        "ID" : 1,
        "Name" : "Doe, John",
        "NetID" : "JXD12345",
        "Email Address" : "JOHN.DOE@EXAMPLE.EDU",
        "Group" : 1,
    },{
        "ID" : 2,
        "Name" : "Alec, Curry",
        "NetID" : "AMC53511",
        "Email Address" : "ALEC.CURRY@EXAMPLE.EDU",
        "Group" : 2,
    }]
    students_df = pd.DataFrame(data=students).set_index("ID")
    result = generate_gradebook(students_df=students_df)
    assert list(result.keys()) == [1, 2]
    
    
def test_results_group_contains_students_net_id_lowercase():
    students = [
        {
            "ID": 1,
            "Name": "Doe, John",
            "NetID": "JXD12345",
            "Email Adress": "JOHN.DOE@EXAMPLE.EDU",
            "Group": 1,
        },
        {
            "ID": 2,
            "Name": "Doe, Second",
            "NetID": "SXD54321",
            "Email Adress": "SECOND.DOE@EXAMPLE.EDU",
            "Group": 1,
        },
    ]
    students_df = pd.DataFrame(data=students).set_index("ID")

    result = generate_gradebook(students_df=students_df)

    assert result[1]["net_id"].to_list() == ["jxd12345", "sxd54321"]