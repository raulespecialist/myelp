from django.test import TestCase
from .models import Business, User, Review
from faker import Faker


class ReviewTest(TestCase):
    """
        Test model Review
    """
    def setUp(self):
        """
            User Creation
        """
        self.fake = Faker()
        self.review = Review.objects.create(
            #review_id='jsjHGJjjkkkk',
            user=User(user_id='dacAIZ6fTM6mqwW5uxkskg'),
            business=Business(business_id='ikCg8xy5JIg_NGPx-MSIDA'),
            stars=self.fake.random_int(min=0, max=5),
            useful=self.fake.random_int(min=0, max=5),
            funny=self.fake.random_int(min=0, max=5),
            cool=self.fake.random_int(min=0, max=5),
            text=self.fake.text(),
            date=self.fake.date_object()
        )
        self.count = Review.objects.count() - 1

    def test_save_model(self):
        """
            Count the number de users
        """
        saved_models = Review.objects.count()
        self.assertEqual(saved_models, self.count + 1)
    def test_update_model(self):
        """
            Update a review
        """
        review = Review.objects.all()
        review.update(funny=2)

        review = Review.objects.all().first()
        self.assertEqual(review.funny, 2)

    def test_delete_models(self):
        """
            Delete a review
        """
        review = Review.objects.all()
        review.delete()

        saved_models = Review.objects.count()
        self.assertEqual(saved_models, self.count)

