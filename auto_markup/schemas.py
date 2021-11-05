from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TheNews(BaseModel):
    title: str = Field(..., example="Бесстрашные бойцы и сладкоежки: в Московском зоопарке поселились медоеды", max_length=300)
    preview_text: str = Field(..., example="Медоеды известны своей смелостью. В случае если их жизни что-то угрожает, они без колебаний идут в атаку. Они запросто могут напасть на льва, леопарда и буйвола, им нипочем яд кобры и скорпиона.", max_length=1000)
    full_text: str = Field(..., example="Один из самых известных отморозков животного мира. Только медоед способен вести схватку, один против шести львов. Есть королевских кобр. Периодически драться с леопардами. Он имеет настолько сильную иммунную систему, что даже после смертельного укуса кобры он просто засыпает, а проснувшись дальше продолжает, есть эту же кобру.")


class MarkUp(BaseModel):
    tags: Optional[List[str]]
    spheres: Optional[List[str]]

    class Config:
        orm_mode = True


class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    exception: str = None


class TheFullNews(TheNews, MarkUp):
    based_tags: Optional[List[str]]
    based_spheres: Optional[List[str]]
