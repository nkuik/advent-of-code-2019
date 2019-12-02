import pytest

from opcode_handler import handle_input


def test_first_case_opcode():
    input = "1,9,10,3,2,3,11,0,99,30,40,50"
    expected_output = "3500,9,10,70,2,3,11,0,99,30,40,50"
    
    assert expected_output == handle_input(input) 

def second_case_opcode():
    input = "1,1,1,4,99,5,6,0,99"
    expected_output = "30,1,1,4,2,5,6,0,99"
    
    assert expected_output == handle_input(input) 