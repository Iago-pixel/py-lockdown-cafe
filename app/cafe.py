from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import date


class Cafe:
  def __init__(self, name: str) -> None:
    self.name = name

  def visit_cafe(self, visitor: dict) -> str:
    if not "vaccine" in visitor:
      raise NotVaccinatedError(f"Visitor {visitor.get('name', 'unknown')} cannot enter {self.name}: not vaccinated.")
    elif date.today() > visitor["vaccine"]["expiration_date"]:
      raise OutdatedVaccineError(f"Visitor {visitor.get('name', 'unknown')} cannot enter {self.name}: expired vaccine {visitor["vaccine"]["expiration_date"].strftime("%Y-%m-%d")}")
    elif not visitor.get("wearing_a_mask"):
      raise NotWearingMaskError(f"Visitor {visitor.get('name', 'unknown')} cannot enter {self.name}: need to wear a mask")
    return f"Welcome to {self.name}"
