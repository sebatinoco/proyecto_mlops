from pydantic import BaseModel

# Model Input Schema
class InputData(BaseModel):
    year: int
    week: int
    customer_id: str
    product_id: str
    region_id: str
    zone_id: str
    customer_type: str
    Y: float
    X: float
    num_deliver_per_week: int
    num_visit_per_week: int
    brand: str
    category: str
    sub_category: str
    segment: str
    package: str
    size: float

input_example = InputData(
    year=2024,
    week=1,
    customer_id="25734",
    product_id="1370",
    region_id="80",
    zone_id="5148",
    customer_type="ABARROTES",
    Y=-46.451260,
    X=-107.099790,
    num_deliver_per_week=2,
    num_visit_per_week=3,
    brand="Brand 34",
    category="BEBIDAS CARBONATADAS",
    sub_category="GASEOSAS",
    segment="MEDIUM",
    package="BOTELLA",
    size=10.0
)