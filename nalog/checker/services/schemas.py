from pydantic import BaseModel, Field

from .config import service_settings


class Row(BaseModel):
    A: str = Field(None, min_length=1, max_length=100, alias="branch")
    B: str = Field(None, min_length=1, max_length=100, alias="employee")
    C: float = Field(None, alias="tax_base")
    D: float = Field(None, alias="actual_tax_calculated")
    E: float = Field(None, alias="correct_tax_calculated")
    F: float = Field(None, alias="difference")

    def calculated_empty_fields(self):
        if service_settings.tax.increased_level >= self.C:
            self.E = self.C * service_settings.tax.normal_rate
        else:
            tmp = self.C - service_settings.tax.increased_level
            self.E = (
                service_settings.tax.increased_level
                * service_settings.tax.normal_rate
                + tmp * service_settings.tax.increased_rate
            )
        self.E = round(self.E, ndigits=4)
        self.F = round((self.D - self.E), ndigits=4)
