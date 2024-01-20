import pandas as pd 
import pytest 
from typing import cast

def _create_group(raw_students_group:pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    return result.assign(
        net_id = raw_students_group["NetID"].str.lower(),
        email_address = raw_students_group['Email Address'].str.lower(),
        first_name=raw_students_group["Name"].str.split(", ", expand=True)[1],
        last_name=raw_students_group["Name"].str.split(", ", expand=True)[0],
    )

def generate_gradebook(students_df:pd.DataFrame) -> dict[int, pd.DataFrame]:
    return {
        cast(int, group): _create_group(raw_students_group=table)
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
    

    
@pytest.fixture
def two_students_in_the_same_group() -> pd.DataFrame():
    students = [
        {
            "ID": 1,
            "Name": "Doe, John",
            "NetID": "JXD12345",
            "Email Address": "JOHN.DOE@EXAMPLE.EDU",
            "Group": 1,
        },
        {
            "ID": 2,
            "Name": "Doe, Second",
            "NetID": "SXD54321",
            "Email Address": "SECOND.DOE@EXAMPLE.EDU",
            "Group": 1,
        }
    ]
    return pd.DataFrame(data=students).set_index("ID")

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
    
def test_results_group_contains_students_net_id_lowercase(two_students_in_the_same_group):
    
    result = generate_gradebook(students_df=two_students_in_the_same_group)
    assert result[1]["net_id"].to_list() == ["jxd12345", "sxd54321"]
    
    
def test_results_group_contains_students_email_address_lowercase(two_students_in_the_same_group):

    result = generate_gradebook(students_df = two_students_in_the_same_group)
    assert result[1]['email_address'].to_list() == [ 
                                                    'john.doe@example.edu',
                                                    'second.doe@example.edu'
    ]   
def test_results_group_contains_students_first_name(
    two_students_in_the_same_group,
):
    result = generate_gradebook(students_df=two_students_in_the_same_group)

    assert result[1]["first_name"].to_list() == [
        "John",
        "Second",
    ]


def test_results_group_contains_students_last_name(
    two_students_in_the_same_group,
):
    result = generate_gradebook(students_df=two_students_in_the_same_group)

    assert result[1]["last_name"].to_list() == [
        "Doe",
        "Doe",
    ]