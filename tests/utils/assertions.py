
def assert_sorted(actual_list, reverse=False, message="List is not sorted"):
    expected = sorted(actual_list, reverse=reverse)
    assert actual_list == expected, f"{message}. Got: {actual_list}"
    