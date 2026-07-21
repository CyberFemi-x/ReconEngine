from dataclasses import dataclass, asdict

@dataclass
class AssetRecord:
    """
    Represents one normalized discovery record.
    """

    observed_at: str
    target: str
    port: int
    protocol: str
    service: str
    source_tool: str
    source_file: str
    confidence: float
    notes: str