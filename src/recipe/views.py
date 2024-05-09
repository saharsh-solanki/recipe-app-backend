from base.views import BaseViewSet
from src.recipe import serializers
from src.recipe import filters
from src.recipe.models import Recipe, Review, RecipeCategory, Rating


class RecipeViewSet(BaseViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    filterset_class = filters.RecipeFilter
    search_fields = ("title", "description")


class RatingViewSet(BaseViewSet):
    serializer_class = serializers.RatingSerializer
    queryset = Rating.objects.all()
    filterset_class = filters.RatingFilter


class ReviewViewSet(BaseViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = Review.objects.all()
    filterset_class = filters.ReviewFilter


class RecipeCategoryViewSet(BaseViewSet):
    serializer_class = serializers.RecipeCategorySerializer
    queryset = RecipeCategory.objects.all()
    filterset_class = filters.RecipeCategoryFilter
