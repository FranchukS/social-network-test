from django.test import TestCase

# Create your tests here.

# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from rest_framework import status
# from rest_framework.test import APIClient, APITestCase
#
# from .models import Post
#
#
# class PostModelTest(TestCase):
#     """Test for the post model"""
#
#     def setUp(self):
#         test_user = get_user_model().objects.create(
#             username='testuser', password='abcd1234')
#         test_user.save()
#
#         test_post = Post.objects.create(
#             title='Test', body='Hello world', author=test_user)
#         test_post.save()
#
#     def test_post_content(self):
#         post = Post.objects.get(id=1)
#         username = f'{post.author}'
#         self.assertEqual(post.title, 'Test')
#         self.assertEqual(post.body, 'Hello world')
#         self.assertEqual(username, 'testuser')
#
#
# class PostViewTest(APITestCase):
#     """Test for the api views"""
#
#     def setUp(self):
#         self.client = APIClient()
#         self.url = '/api/v1/posts/'
#         self.wrong_url = '/api/posts/'
#         self.user = get_user_model().objects.create(
#             username='testuser', password='abcd1234')
#         self.post = Post.objects.create(
#             title='Test title', body='Test body', author=self.user)
#         self.post_with_like = Post.objects.create(
#             title='Title test', body='Body test', author=self.user)
#         self.client.force_authenticate(user=self.user)
#
#     def test_post_list(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_post_list_not_found(self):
#         response = self.client.get(self.wrong_url)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_post_create(self):
#         response = self.client.post(
#             self.url,
#             {'title': 'Test title', 'body': 'Test body', 'author': self.user.id},
#             format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_post_detail(self):
#         response = self.client.get(f'{self.url}{self.post.pk}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_post_detail_update(self):
#         response = self.client.put(
#             f'{self.url}{self.post.pk}/',
#             {
#                 'title': 'Test title edited',
#                 'body': 'Test body edited',
#                 'author': self.user.id
#             },
#             format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_post_detail_delete(self):
#         response = self.client.delete(f'{self.url}{self.post.pk}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_post_like(self):
#         response = self.client.put(
#             f'{self.url}{self.post.pk}/like/',
#             {
#                 'user': self.user.id,
#                 'post': self.post.id,
#                 'post_like': True
#             },
#             format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_post_unlike(self):
#         self.client.put(
#             f'{self.url}{self.post_with_like.pk}/like/',
#             {
#                 'user': self.user.id,
#                 'post': self.post_with_like.id,
#                 'post_like': True
#             },
#             format='json')
#         response = self.client.delete(f'{self.url}{self.post_with_like.pk}/unlike/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)