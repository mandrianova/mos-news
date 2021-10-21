from fastapi import APIRouter, HTTPException

from auto_markup.model import get_result_tag_and_spheres_for_title_preview_fulltext, update_model_func
from auto_markup.schemas import MarkUp, TheNews


auto_markup = APIRouter(prefix='/auto_markup', tags=["auto_markup"])


@auto_markup.post("/get_markups", response_model=MarkUp)
async def generate_markups(news: TheNews):
    tags, spheres = get_result_tag_and_spheres_for_title_preview_fulltext(
        title=news.title,
        preview=news.preview_text,
        full_txt=news.full_text
    )
    return MarkUp(tags=tags, spheres=spheres)


@auto_markup.post("/update_model")
async def update_model(update: bool):
    if update is True:
        result = update_model_func()
        if result is None:
            raise HTTPException(status_code=400, detail="Error, check logs")
        return {'message': 'model updated'}
    elif update is False:
        return {'message': 'if you want to update the model - set it true'}
