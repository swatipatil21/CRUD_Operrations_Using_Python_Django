import re

# validation
text1 = re.compile("^[a-zA-Z]+$")
text_space = re.compile("^[a-zA-Z ]*$")
number = re.compile("^[0-9]+$")
dob = re.compile("^(?:1[01][0-9]|120|1[7-9]|[2-9][0-9])$")
dateFormat =re.compile("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$")
alphanumeric = re.compile("^[a-zA-Z0-9_]+$")
alphanumeric_space = re.compile("^[a-zA-Z0-9 ]+$")

