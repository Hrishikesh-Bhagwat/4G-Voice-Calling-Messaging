from pydantic import BaseModel
from typing import List

class ColumnHeading(BaseModel):
    title: str
    file: str

class ColumnRow(BaseModel):
    text: str
    file: str
    id: str
    selected: bool

class Column(BaseModel):
    heading: ColumnHeading
    entries: List[ColumnRow]

class TableResponseModel(BaseModel):
    text: str
    status: bool
    col1: Column
    col2: Column
    col3: Column
    col4: Column
    col5: Column
    col6: Column