from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel, Field


class TheNewsIn(BaseModel):
    title: str = Field(..., example="Бесстрашные бойцы и сладкоежки: в Московском зоопарке поселились медоеды", max_length=300)
    preview_text: str = Field(..., example="Медоеды известны своей смелостью. В случае если их жизни что-то угрожает, они без колебаний идут в атаку. Они запросто могут напасть на льва, леопарда и буйвола, им нипочем яд кобры и скорпиона.", max_length=1000)
    full_text: str = Field(..., example="very long text with unlimited length")


class Sphere(BaseModel):
    id: int
    title: str
    special: bool
    activated: bool
    priority: int


class Tag(BaseModel):
    id: int
    title: str
    created_at: datetime


class Kind(BaseModel):
    id: str
    title: str
    type: int


class Theme(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    icon_id: int
    url: str


class Image(BaseModel):
    id: int
    title: str
    src: str
    width: int
    height: int
    type: str


class TheNewsOut(BaseModel):
    id: int
    title: str
    importance: Optional[str] = None
    published_at: datetime
    created_at: datetime
    updated_at: datetime
    is_deferred_publication: bool
    status: str
    ya_rss: bool                                    # check 
    active_from: Optional[float] = None             # check
    active_to: Optional[float] = None               # check
    oiv_id: Optional[int] = None
    search: int
    display_image: bool
    label: Optional[str] = None
    icon_id: Optional[int] = None
    canonical_url: Optional[str] = None
    canonical_updated_at: Optional[datetime] = None
    is_powered: bool
    has_image: bool
    date: datetime
    has_district: bool
    date_timestamp: datetime
    tags: List[Tag]
    theme_id: Optional[int] = None
    theme_ids: list
    themes: List[Theme]
    spheres: List[Sphere]
    sphere: Sphere
    kind: Kind
    is_oiv_publication: bool
    organizations: list
    updated_at_timestamp: datetime
    created_at_timestamp: datetime
    attach: list                                    # check: gallery, marker, cropboxdata
    active_from_timestamp: bool
    active_to_timestamp: bool
    image: Optional[Dict] = None                     # id, title, copyright + a bunch of type Image
    counter: Optional[float] = None  # check
    territory_area_id: Optional[int] = None
    territory_district_id: Optional[int] = None
    preview_text: str
    full_text: str
    url: str
    preview: Optional[str] = None                 # == preview text
    text: Optional[str] = None                    # == full text
    promo: Optional[bool] = None                  # == 
    images: Optional[str] = None                  # == image


class Recommendation(BaseModel):
    id: int
    title: int
    date: datetime
