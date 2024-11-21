import pytest
from src.XmlDataReader import XmlDataReader
from src.Types import DataType

class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data(self, tmpdir) -> tuple[str, DataType]:
        content = """<?xml version="1.0" encoding="UTF-8" ?>
        <root>
            <Иванов Иван>
                <математика>100</математика>
                <литература>100</литература>
            </Иванов Иван>
            <Петров Петр>
                <химия>80</химия>
                <физика>60</физика>
            </Петров Петр>
        </root>
        """
        data = {
            "Иванов Иван": [("математика", 100), ("литература", 100)],
            "Петров Петр": [("химия", 80), ("физика", 60)],
        }
        path = tmpdir.join("data.xml")
        path.write(content)
        return str(path), data

    def test_read(self, file_and_data):
        path, expected = file_and_data
        result = XmlDataReader().read(path)
        assert result == expected
