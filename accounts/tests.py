from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

class AuthenticationUserTests(TestCase): # Unit Test
    def test_create_user_valid_input(self):
        User = get_user_model()
        test_user = User.objects.create_user(
            username="testuser", password="Welcome55#"
        )
        self.assertEqual(test_user.username, "testuser")
        #self.assertEqual(test_user.password, "Welcome55#")
        self.assertTrue(test_user.is_active)

    def test_create_user_invalid_input(self):
        User = get_user_model()
        test_user = User.objects.create_user(
            username="other_test_user", password="WWelcome55#"
        )
        self.assertNotEqual(test_user.username, "testuser")
        self.assertNotEqual(test_user.password, "Welcome55#")
        self.assertTrue(test_user.is_active)

class DatabaseGrab(TestCase):
    def test_database_fetch(self):
        User = get_user_model()
        test_user = User.objects.create_user(
            username="test", password="Test1!", bio = "testing bio"
        )
        self.assertEqual(test_user.bio, "testing bio")
        self.assertTrue(test_user.is_active)

# BEFORE CHANGES
# Name                                  Stmts   Miss  Cover
# ---------------------------------------------------------
# accounts/__init__.py                      0      0   100%
# accounts/admin.py                        12      0   100%
# accounts/apps.py                          4      0   100%
# accounts/forms.py                        10      0   100%
# accounts/migrations/0001_initial.py       8      8     0%
# accounts/migrations/__init__.py           0      0   100%
# accounts/models.py                        4      0   100%
# accounts/tests.py                         3      0   100%
# accounts/urls.py                          3      0   100%
# accounts/views.py                         7      0   100%
# ---------------------------------------------------------
# TOTAL                                    51      8    84%

# AFTER CHANGES
# Name                                  Stmts   Miss  Cover
# ---------------------------------------------------------
# accounts/__init__.py                      0      0   100%
# accounts/admin.py                        12      0   100%
# accounts/apps.py                          4      0   100%
# accounts/forms.py                        10      0   100%
# accounts/migrations/0001_initial.py       8      0   100%
# accounts/migrations/__init__.py           0      0   100%
# accounts/models.py                        4      0   100%
# accounts/tests.py                        21      0   100%
# accounts/urls.py                          3      0   100%
# accounts/views.py                         7      0   100%
# ---------------------------------------------------------
# TOTAL                                    69      0   100%
