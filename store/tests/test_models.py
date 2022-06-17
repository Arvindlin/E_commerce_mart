from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        """
        Creation of test data.
        """
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributs.
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model(self):
        """
        Test category model return __str__ function i.e, name.
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self) -> None:
        '''Setting up and creating data in Product Model.'''
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data = Product.objects.create(category_id=1, title='new title', created_by_id=1,
                                           slug='new-title', price='20.00', image='django')

    def test_product_model_entry(self):
        """
        Test category model return __str__ function i.e, name.
        """
        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'new title')
