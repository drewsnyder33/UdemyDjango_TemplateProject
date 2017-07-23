from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """

    return value.replace(arg,'')

# below, first 'cut' is the name you're giving this filter, to use when
# calling it in a template
# second cut is calling the actual function we just defined above in this module
register.filter('cut',cut)

# Other way to register this filter would be to use the following decorator
# above the function definition, instead of that last "register.filter" line:
# @register.filter(name='cut')
