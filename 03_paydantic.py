
from pydantic import BaseModel, EmailStr, Field, AnyUrl
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(max_length=50, title="Name of the patient")
    ]
    email: EmailStr
    linkedin: AnyUrl
    age: int
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = None
    contact_detail: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)


patient_info = {
    'name': 'riya',
    'email': 'anu@example.com',
    'linkedin': 'https://www.linkedin.com/in/example',
    'age': 40,
    'weight': 34.5,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_detail': {
        'email': 'anu@example.com',
        'phone': '9876543210'
    }
}

p1 = Patient(**patient_info)
insert_patient_data(p1)
