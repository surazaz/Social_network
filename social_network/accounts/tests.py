from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTests(TestCase):
	def setUp(self):
		self.user1=User(username="surazaz")
		self.user2=User(username="surazaz")
		self.user3=User(email="suraj@gmail.com")
	def test_user_is_active(self):
		# user1=User(username="surazaz")
		# user2=User(username="surazaz")
		# print(user1)
		# self.assertEqual(user1.is_superuser,True)
		# self.assertEqual(user2.is_superuser,True)
		self.assertEqual(self.user1.is_active,True)
		self.assertEqual(self.user2.is_active,True)
		self.assertEqual(self.user3.is_active,True)
	def test_user_is_superuser(self):
		# user1=User(username="surazaz")
		self.assertEqual(self.user1.is_superuser,False)
		self.assertEqual(self.user2.is_superuser,False)
		self.assertEqual(self.user3.is_superuser,False)
	def test_users_are_identical(self):
		self.assertEqual(self.user1.username,self.user2.username)
		# self.assertEqual(self.user1.username,self.user3.username)