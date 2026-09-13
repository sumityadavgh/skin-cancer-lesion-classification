from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from .model_loader import predict_image


@api_view(["POST"])
def predict(request):

    # Check whether an image was uploaded
    if "image" not in request.FILES:
        return Response(
            {"error": "No image uploaded."},
            status=status.HTTP_400_BAD_REQUEST
        )

    image = request.FILES["image"]

    try:
        # Send image to our trained model
        predicted_class, confidence = predict_image(image)

        return Response({
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def home(request):
    return render(request, "index.html")