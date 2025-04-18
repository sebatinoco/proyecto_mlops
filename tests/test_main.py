import os
import sys
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# Agrega la ruta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

# ---------- Fixtures ----------


@pytest.fixture
def sample_input():
    """
    Fixture que retorna un conjunto de datos de entrada válido para el endpoint /predict.

    Returns:
        dict: Diccionario con todos los campos requeridos para una predicción válida.
    """
    return {
        "year": 2024,
        "week": 16,
        "customer_id": "C123",
        "product_id": "P456",
        "region_id": "R01",
        "zone_id": "Z01",
        "customer_type": "Retail",
        "Y": 1.23,
        "X": 4.56,
        "num_deliver_per_week": 2,
        "num_visit_per_week": 3,
        "brand": "BrandA",
        "category": "CatA",
        "sub_category": "SubCatA",
        "segment": "SegmentA",
        "package": "PackA",
        "size": 500.0,
    }


# ---------- Test Cases ----------


def test_home():
    """
    Verifica que el endpoint raíz ('/') esté funcionando correctamente.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world!"}


def test_test_endpoint():
    """
    Verifica que el endpoint '/test' esté funcionando correctamente.
    """
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == "Test endpoint is working!"


def test_predict(sample_input):
    """
    Verifica que el endpoint '/predict' retorne una predicción válida con datos correctos.
    """
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert isinstance(response.json(), (float, int))


def test_predict_missing_field(sample_input):
    """
    Verifica que el endpoint falle adecuadamente si falta un campo requerido.
    """
    bad_input = sample_input.copy()
    del bad_input["year"]

    response = client.post("/predict", json=bad_input)
    assert response.status_code == 422


def test_predict_invalid_data_type(sample_input):
    """
    Verifica que el endpoint falle si se envía un tipo de dato incorrecto.
    """
    bad_input = sample_input.copy()
    bad_input["year"] = "not_a_number"

    response = client.post("/predict", json=bad_input)
    assert response.status_code == 422


def test_predict_extreme_values(sample_input):
    """
    Verifica el comportamiento del endpoint ante valores extremos pero válidos.
    """
    extreme_input = sample_input.copy()
    extreme_input["size"] = -1000.0

    response = client.post("/predict", json=extreme_input)
    assert response.status_code == 200
    assert isinstance(response.json(), (float, int))


def test_predict_response_format(sample_input):
    """
    Verifica el formato de la respuesta del endpoint '/predict'.
    """
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    prediction = response.json()
    assert isinstance(prediction, (float, int))


def test_predict_model_not_loaded(sample_input):
    """
    Simula un error en la carga del modelo y verifica el manejo del error.
    """
    with patch("main.model", None):
        response = client.post("/predict", json=sample_input)
        assert response.status_code == 422
        assert "error" in response.json()
