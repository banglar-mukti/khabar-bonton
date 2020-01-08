from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@dj.com',
            password='test123')
        self.assertEquals(user.username, 'test')
        self.assertEquals(user.email, 'test@dj.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='admin',
            email='admin@dj.com',
            password='admin123')
        self.assertEquals(user.username, 'admin')
        self.assertEquals(user.email, 'admin@dj.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)