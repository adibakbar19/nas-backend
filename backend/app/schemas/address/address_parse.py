from pydantic import BaseModel, Field


class AddressParseRequest(BaseModel):
    address: str | None = Field(default=None, examples=["No 12, Jln Ampang, 50450 Kuala Lumpur"])
    addresses: list[str] | None = Field(default=None)
    text: str | None = Field(default=None, description="Line-separated addresses.")
    csv_text: str | None = Field(default=None, description="CSV payload containing an address column.")
    csv_address_column: str | None = Field(default=None)
    use_ai: bool = Field(default=True)
    require_mukim: bool = Field(default=True)
    ai_min_confidence: float = Field(default=0.85, ge=0.0, le=1.0)
    max_records: int = Field(default=100, ge=1, le=1000)


class AddressParseItem(BaseModel):
    record_id: str | None = None
    source_address: str | None = None
    standardized_address: dict
    confidence_score: float
    confidence_band: str | None = None
    matched: bool
    match_status: str
    visual_indicator: str
    reason_codes: list[str] = Field(default_factory=list)
    correction_notes: list[str] = Field(default_factory=list)
    parser_mode: str | None = None
    ai_model: str | None = None
    ai_reason: str | None = None


class AddressParseResponse(BaseModel):
    count: int
    ai_attempted: bool
    ai_model: str | None = None
    counts: dict[str, int]
    items: list[AddressParseItem]
