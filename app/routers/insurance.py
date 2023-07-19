from fastapi import APIRouter, status, HTTPException
import schemas, CRUD

insurance_router = APIRouter(prefix='/api/insurance', tags=['Insurance'])


@insurance_router.post('/calculate')
async def calculate_insurance_cost(insurance_data: schemas.InsuranceData):
    tariff_cost = CRUD.calculate(insurance_data)
    if tariff_cost:
        return tariff_cost
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'There was no tariff with type of {insurance_data.cargo_type} on {insurance_data.tariff_date}')
