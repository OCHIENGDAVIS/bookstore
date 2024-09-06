from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserModelTests(TestCase):
    def test_Create_user(self):
        user = User.objects.create(
            username='will',
            email='will@gmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        super_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@gmail.com',
            password='pass1234'
        )
        self.assertEqual(super_user.username, "superadmin")
        self.assertEqual(super_user.email, "superadmin@gmail.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)

