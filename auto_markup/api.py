from fastapi import APIRouter
from auto_markup.model import get_result_tag_and_spheres_for_title_preview_fulltext
from auto_markup.schemas import MarkUp, TheNews, TheFullNews
from auto_markup.services import get_one_news_from_mos_api

auto_markup = APIRouter(prefix='/auto_markup', tags=["auto_markup"])


@auto_markup.post("/generate_markups", response_model=MarkUp)
async def generate_markups(news: TheNews):
    """
    Generate a markup (**tags** and **spheres**) for this **news**:
    **Input**
    - **title**: title
    - **preview_text**: preview text
    - **full_text**: full text

    **Output**
    - **tags**: all prediction tags for this text
    - **spheres**: all prediction spheres for this text
    """
    tags, spheres = get_result_tag_and_spheres_for_title_preview_fulltext(
        title=news.title,
        preview=news.preview_text,
        full_txt=news.full_text
    )
    return MarkUp(tags=tags, spheres=spheres)


@auto_markup.get("/get_one_news/{news_id}", response_model=TheFullNews)
async def get_one_news(news_id: int):
    """
    Get one news all fields (**title**, **preview text**, **full text**, **based tags**, **based spheres**,
     **gen tags**, **gen spheres**) for this **news**:
    **Input**
    - **news_id**: news_id

    **Output**
    - **title**: TITLE
    - **preview**: PREVIEW
    - **full text**: TEXT
    - **based tags**: inserted TAGS by person
    - **based spheres**: inserted SPHERES by person
    - **gen tags**: all prediction spheres for this text
    - **gen spheres**: all prediction spheres for this text

    """
    data = get_one_news_from_mos_api(news_id)
    gen_tags, gen_spheres = get_result_tag_and_spheres_for_title_preview_fulltext(
        title=data['title'],
        preview=data['preview_text'],
        full_txt=data['full_text']
    )

    return TheFullNews(
        title=data['title'],
        preview_text=data['preview_text'],
        full_text=data['full_text'],
        based_tags=data['tags'],
        based_spheres=data['spheres'],
        tags=gen_tags,
        spheres=gen_spheres
    )