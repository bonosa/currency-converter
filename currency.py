"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Saroj Bono
Date:   05/10/2023
"""
import introcs
APIKEY='JOUyWipQsbBKZbI6pvu0uttU1SvOX9pD4Pj4zs5ci48e'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.
    
    Example: before_space('Hello World') returns 'Hello'
    
    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    introcs.assert_equals(True, ' ' in s)
    index_of_space = introcs.find_str(' ')
    return s[:index_of_space]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    introcs.assert_equals(True, ' ' in s)
    index_of_space = introcs.find_str(' ')
    return s[index_of_space+1:]    

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string. So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    # Enforce precondition
    introcs.assert_equals(True, s.count('"') >= 2)

    # Find the first and second quote indices
    first_quote_index = introcs.find_str(s, '"')
    second_quote_index = introcs.find_str(s, '"', first_quote_index + 1)

    # Return the substring between the two quote indices
    return s[first_quote_index + 1:second_quote_index]

def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. 

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    # Enforce precondition
    introcs.assert_equals(str, type(json))

    # Find the start index of the src value
    src_index = introcs.find_str(json, '"src"')
    first_quote_index = introcs.find_str(json, '"', src_index + 4)
    second_quote_index = introcs.find_str(json, '"', first_quote_index + 1)

    # Return the substring between the two quote indices
    return json[first_quote_index + 1:second_quote_index]

def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. 

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    # Enforce precondition
    introcs.assert_equals(str, type(json))

    # Find the start index of the dst value
    dst_index = introcs.find_str(json, '"dst"')
    first_quote_index = introcs.find_str(json, '"', dst_index + 4)
    second_quote_index = introcs.find_str(json, '"', first_quote_index + 1)

    # Return the substring between the two quote indices
    return json[first_quote_index + 1:second_quote_index]

def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. 

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    # Enforce precondition
    introcs.assert_equals(str, type(json))

    # Find the start index of the error value
    error_index = introcs.find_str(json, '"error"')
    first_quote_index = introcs.find_str(json, '"', error_index + 6)
    second_quote_index = introcs.find_str(json, '"', first_quote_index + 1)

    # Check if there's an error message
    return json[first_quote_index + 1:second_quote_index] != ''


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    # Enforce preconditions
    introcs.assert_equals(True, type(src) == str and src != '')
    introcs.assert_equals(True, type(dst) == str and dst != '')
    introcs.assert_float(amt)

    # Create the query string
    query = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + src + '&to=' + dst + '&amt=' + str(amt) + '&key'=key1

    # Get the response
    response = introcs.urlread(query)

    # Return the response
    return response

def get_dst(json):
    

    # enforce preconditions
    introcs.assert_equals(True, isinstance(json, str))
    
    # find the '"dst"' substring in the json string
    dst_index = introcs.find_str(json, '"dst"')
    
    # return the substring after '"dst"'
    return first_inside_quotes(json[dst_index + 6:])



