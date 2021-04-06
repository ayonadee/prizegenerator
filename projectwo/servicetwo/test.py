from unittest.mock import patch
from flask_testing import TestCase

with patch('account_number') as f:
    f.return_value = [10, 5, 3, 7, 5, 4]