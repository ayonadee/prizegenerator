from unittest.mock import patch
from flask_testing import TestCase


with patch('random_letter') as a:
    a.return_value = ['abcd']