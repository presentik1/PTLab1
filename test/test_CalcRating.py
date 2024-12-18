# -*- coding: utf-8 -*-
from typing import Dict, Tuple
from src.Types import DataType
from src.CalcRating import CalcRating
import pytest

RatingsType = Dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100),
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97),
            ],
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000,
        }

        return data, rating_scores

    def test_init_calc_rating(
        self, input_data: Tuple[DataType, RatingsType]
    ) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: Tuple[DataType, RatingsType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student, rating_score in rating.items():
            assert pytest.approx(
                rating_score, abs=0.001
            ) == input_data[1][student]
