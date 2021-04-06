from unittest.mock import patch
from flask_testing import TestCase


with patch('empty_letter_list') as a:
    a.return_value = ['abcd']