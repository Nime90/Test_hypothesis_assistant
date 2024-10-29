def find_dep_ind_var(response):
    import re
    # Patterns for extracting relevant values
    test_pattern = r"Test:\s*([^,]+)"
    dependent_var_pattern = r"Dependent Var\s*([^,]+)"
    independent_var_pattern = r"Independent Var\s*(.*)"


    # Extract using regular expressions with case insensitivity
    response_final=response[response.find('Test:'):]
    test = re.search(test_pattern, response_final, re.IGNORECASE)
    dependent_var = re.search(dependent_var_pattern, response_final, re.IGNORECASE)
    independent_var_string = re.search(independent_var_pattern, response_final, re.IGNORECASE)

    # Store values in variables if they are found
    test_name = test.group(1).strip() if test else None
    dependent_variable = dependent_var.group(1).strip().replace(',','').replace('.','') if dependent_var else None
    independent_variable = independent_var_string.group(1).strip().split(':')[1].strip().replace(',','').replace('.','').split(' ')
    return test_name, dependent_variable, independent_variable