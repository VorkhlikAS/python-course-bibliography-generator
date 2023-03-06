"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):
    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class NormativeActModel(BaseModel):
    """
    Модель нормативно-правового акта:

    .. code-block::

        NormativeActModel(
            type="Указ Президента Рос. Федерации",
            title="О мерах по противодействию коррупции",
            acceptance_date="19.05.2008",
            number="815",
            publication_source="Собрание законодательства Российской Федерации",
            publication_year=2008,
            source_number=21,
            article_number=2429,
            edition_date="3.07.2019"
        )
    """

    type: str
    title: str
    acceptance_date: str
    number: str
    publication_source: str
    publication_year: int = Field(..., gt=0)
    source_number: int = Field(..., gt=0)
    article_number: int = Field(..., gt=0)
    edition_date: Optional[str]


class DissertationModel(BaseModel):
    """
    Модель диссертации:

    .. code-block::

        DissertationModel(
            author="Белозеров И.В.",
            article_title="Религиозная политика Золотой Орды на Руси в XIII - XIV вв.",
            author_degree="канд.",
            science_branch="ист. наук",
            branch_code="07.00.02",
            city="М.",
            year=2002,
            page_count=215,
        )
    """

    author: str
    article_title: str
    author_degree: str
    science_branch: str
    branch_code: str
    city: str
    year: int = Field(..., gt=0)
    page_count: int = Field(..., gt=0)
