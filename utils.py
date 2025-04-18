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
