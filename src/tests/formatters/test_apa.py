"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NormativeActModel,
    DissertationModel,
)
from formatters.styles.apa import (
    APABook,
    APACollectionArticle,
    APAInternetResource,
    APANormativeAct,
    APADissertation,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.
        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство (3-е изд. – ) СПб.: Просвещение, 999 p."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости (01.01.2021) Наука как искусство https://www.vedomosti.ru"
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство, Сборник научных трудов СПб.: АСТ, 25-30 p."
        )

    def test_dissertation(self, dissertation_model_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертации.
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertation(dissertation_model_fixture)
        assert (
            model.formatted == "Иванов И.М. (2020) Наука как искусство / СПб., 999 p."
        )

    def test_normative_act(
        self, normative_act_model_fixture: NormativeActModel
    ) -> None:
        """
        Тестирование форматирования нормативного акта.
        :param NormativeActModel normative_act_model_fixture: Фикстура модели нормативного акта
        :return:
        """

        model = APANormativeAct(normative_act_model_fixture)

        assert (
            model.formatted
            == "(2020) Наука как искусство, Федеральный закон, Научный журнал, 123, edited 01.01.2021"
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        normative_act_model_fixture: NormativeActModel,
        dissertation_model_fixture: DissertationModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.
        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param NormativeActModel normative_act_model_fixture: Фикстура модели нормативного акта
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APACollectionArticle(articles_collection_model_fixture),
            APANormativeAct(normative_act_model_fixture),
            APADissertation(dissertation_model_fixture),
        ]

        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[3]
        assert result[1] == models[1]
        assert result[2] == models[4]
        assert result[3] == models[0]
        assert result[4] == models[2]
