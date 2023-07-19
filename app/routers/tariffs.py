from fastapi import APIRouter, Response, status, HTTPException
import schemas, CRUD

tariff_router = APIRouter(prefix='/api/tariffs', tags=['Tariff'])


@tariff_router.post('/create')
async def create_tariff(tariff: schemas.TariffCreate):
    await CRUD.create(tariff)
    return Response(status_code=status.HTTP_201_CREATED)


@tariff_router.get('/')
async def get_all_tariffs():
    return await CRUD.get_all()


@tariff_router.get('/{tariff_id}')
async def get_tariff_by_id(tariff_id: int):
    tariff = await CRUD.get_by_id(tariff_id)
    if tariff:
        return tariff
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'No tariff with {tariff_id} id')


@tariff_router.put('/{tariff_id}')
async def update_tariff(tariff_id: int, tariff_data: schemas.Tariff):
    updated = await CRUD.update(tariff_id, tariff_data)
    if updated:
        return updated
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'No tariff with {tariff_id} id')


@tariff_router.delete('/delete/{tariff_id}')
async def delete_tariff(tariff_id: int):
    to_delete = await CRUD.delete(tariff_id)
    if to_delete:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'No tariff with {tariff_id} id')
