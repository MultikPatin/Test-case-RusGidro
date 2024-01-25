from pydantic import PositiveInt
from pydantic_settings import BaseSettings


class TaxSettings(BaseSettings):
    normal_rate: float = 0.13
    increased_rate: float = 0.15
    increased_level: PositiveInt = 5_000_000


class FileSettings(BaseSettings):
    iter_config: dict = {
        "min_row": 3,
        "max_col": 6,
    }


class CellsHeaderSettings(BaseSettings):
    merge: dict = {
        "A1:A2": "Филиал",
        "B1:B2": "Сотрудник",
        "C1:C2": "Налоговая база",
        "F1:F2": "Отклонения",
        "D1:E1": "Налог",
    }
    single: dict = {
        "D2": "Исчислено всего",
        "E2": "Исчислено всего по формуле",
    }
    width: dict = {
        "A": 40,
        "B": 30,
        "C": 15,
        "D": 15,
        "E": 18,
        "F": 15,
    }
    height: dict = {1: 20, 2: 20}


class FontSettings(BaseSettings):
    header: dict = {
        "bold": True,
        "color": "000000",
        "name": "Arial",
        "size": 10,
    }


class AlignmentSettings(BaseSettings):
    header: dict = {
        "horizontal": "center",
        "vertical": "center",
        "wrapText": True,
    }


class PatternFillSettings(BaseSettings):
    header: dict = {
        "patternType": "solid",
        "fgColor": "CBE4E5",
    }
    correct: dict = {
        "patternType": "solid",
        "fgColor": "9bbb59",
    }
    incorrect: dict = {
        "patternType": "solid",
        "fgColor": "c0504d",
    }


class ReportSheetSettings(BaseSettings):
    name: str = "Валидации НДФЛ"
    cells: CellsHeaderSettings = CellsHeaderSettings()
    font: FontSettings = FontSettings()
    pattern_fill: PatternFillSettings = PatternFillSettings()
    alignment: AlignmentSettings = AlignmentSettings()


class ReportSettings(BaseSettings):
    file_name: str = "report.xlsx"
    prefix_format: str = "%Y-%m-%d_%H-%M-%S_"
    sheet: ReportSheetSettings = ReportSheetSettings()


class ServiceSettings(BaseSettings):
    report: ReportSettings = ReportSettings()
    file: FileSettings = FileSettings()
    tax: TaxSettings = TaxSettings()


service_settings = ServiceSettings()
