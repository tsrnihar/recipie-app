from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class ModelTests(TestCase):
    

    def test_create_user_with_email_pwd(self):
        email = "test@healthily.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        email = "test@HEALTHILY.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="test123"
            )

    def test_create_super_user(self):
        """Test to check superuser creation"""
        user = get_user_model().objects.create_super_user(
            email="tsrnihar@gmail.com",
            password="test@1234"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
