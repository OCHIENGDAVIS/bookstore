from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm

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


class SignupPageTest(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'
    def setUp(self):
        url  = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'hi there, I should not be on the page')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)