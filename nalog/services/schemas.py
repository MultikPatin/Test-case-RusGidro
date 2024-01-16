from pydantic import BaseModel, Field

NORMAL_TAX_RATE = 0.13
INCREASED_TAX_RATE = 0.15
INCREASED_TAX_LEVEL = 5_000_000
NUMBER_OF_DIGITS = 4


class InputRecord(BaseModel):
    A: str = Field(None, min_length=1, max_length=100, alias="branch")
    B: str = Field(None, min_length=1, max_length=100, alias="employee")
    C: float = Field(alias="tax_base")
    D: float = Field(alias="actual_tax_calculated")
    E: float = Field(alias="correct_tax_calculated")
    F: float = Field(alias="difference")

    def calculated_empty_fields(self):
        if self.C >= INCREASED_TAX_LEVEL:
            self.E = self.C * INCREASED_TAX_RATE
        else:
            self.E = self.C * NORMAL_TAX_RATE
        self.E = round(self.E, ndigits=NUMBER_OF_DIGITS)
        self.F = round((self.D - self.E), ndigits=NUMBER_OF_DIGITS)
