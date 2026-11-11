from django.test import TestCase
from django.urls import reverse
from .models import Box


class BoxRecommendationTest(TestCase):

    def setUp(self):
        Box.objects.create(
            name="Small Box",
            length=15,
            width=15,
            height=15,
            max_weight=3,
            cost=20
        )

        Box.objects.create(
            name="Medium Box",
            length=25,
            width=20,
            height=15,
            max_weight=5,
            cost=35
        )

    def test_small_box_recommendation(self):
        response = self.client.post(reverse('box_recommendation'), {
            'length': 10,
            'width': 10,
            'height': 10,
            'weight': 2
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['recommended_box'].name,
            'Small Box'
        )

    def test_medium_box_recommendation(self):
        response = self.client.post(reverse('box_recommendation'), {
            'length': 20,
            'width': 15,
            'height': 10,
            'weight': 4
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['recommended_box'].name,
            'Medium Box'
        )

    def test_no_suitable_box(self):
        response = self.client.post(reverse('box_recommendation'), {
            'length': 60,
            'width': 50,
            'height': 40,
            'weight': 5
        })

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['recommended_box'])
        self.assertTrue(response.context['searched'])

    def test_weight_exceeds_capacity(self):
        response = self.client.post(reverse('box_recommendation'), {
            'length': 10,
            'width': 10,
            'height': 10,
            'weight': 30
        })

        self.assertIsNone(response.context['recommended_box'])
        
    def test_exact_box_capacity(self):
        response = self.client.post(reverse('box_recommendation'), {
            'length': 15,
            'width': 15,
            'height': 15,
            'weight': 3
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['recommended_box'].name,
            'Small Box'
        )
