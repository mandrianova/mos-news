from fastapi import APIRouter
from auto_markup.model import get_result_tag_and_spheres_for_title_preview_fulltext
from auto_markup.schemas import MarkUp, TheNews

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
