import pytest
from src.XmlDataReader import XmlDataReader
from src.Types import DataType

class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data(self, tmpdir) -> tuple[str, DataType]:
        content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
    <student name="Иванов Иван">
        <subject name="математика">100</subject>
        <subject name="литература">100</subject>
    </student>
    <student name="Петров Петр">
        <subject name="химия">80</subject>
        <subject name="физика">60</subject>
    </student>
</root>
"""
        data = {
            "Иванов Иван": [("математика", 100), ("литература", 100)],
            "Петров Петр": [("химия", 80), ("физика", 60)],
        }
        path = tmpdir.join("data.xml")
        path.write(content)  # Записываем файл
        return str(path), data

    def test_read(self, file_and_data):
        path, expected = file_and_data
        result = XmlDataReader().read(path)
        assert result == expected
