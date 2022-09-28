from pydantic import BaseModel, validator, EmailStr, Field
from decimal import Decimal

class Cadastro(BaseModel):
    name: str
    email: EmailStr
    username: str
    password: str
    age: int = Field(gt=18)


if __name__ == '__main__':
    Cadastro(
    name='samuel colvin',
    email='samuel@gmail.com',
    username='scolvin',
    password='zxcvbn',
    age=19
)
