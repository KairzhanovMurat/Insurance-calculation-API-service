import schemas
from models import Tariff
import decimal


async def create(tariffs_data: schemas.TariffCreate):
    for _date, items in tariffs_data.tariffs.items():
        for item in items:
            tariff = Tariff(
                cargo_type=item.cargo_type,
                rate=item.rate,
                date=_date,
            )
            await tariff.save()


async def get_all():
    return await Tariff.all()


async def get_by_id(tariff_id: int):
    return await Tariff.filter(id=tariff_id).first()


async def update(tariff_id: int, tariff_data: schemas.Tariff):
    updated_tariff = await Tariff.filter(id=tariff_id).first()
    if updated_tariff:
        updated_tariff.date = tariff_data.tariff_date
        updated_tariff.rate = tariff_data.rate
        updated_tariff.cargo_type = tariff_data.cargo_type
        await updated_tariff.save()
        return updated_tariff
    return None


async def delete(tariff_id: int):
    tariff = await Tariff.filter(id=tariff_id).first()
    if tariff:
        await tariff.delete()
        return True
    return None


async def calculate(insurance_data: schemas.InsuranceData):
    tariff = await Tariff.filter(cargo_type=insurance_data.cargo_type.value,
                                 date=insurance_data.tariff_date).first()
    if tariff:
        cost = decimal.Decimal(insurance_data.cost) * tariff.rate
        return {'rate': tariff.rate,
                'cost': cost}
    return None
