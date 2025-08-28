from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import date


class Cafe:
  def __init__(self, name: str) -> None:
    self.name = name

  def visit_cafe(self, visitor: dict) -> None:
    if not "vaccine" in visitor:
      raise NotVaccinatedError("You need to be vaccinated")
    elif date.today() > visitor["vaccine"]["expiration_date"]:
      raise OutdatedVaccineError("Expired vaccine")
    elif not visitor["wearing_a_mask"]:
      raise NotWearingMaskError("You need to wear a mask")
    else:
      return f"Welcome to {self.name}"
