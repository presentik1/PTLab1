from src.DataReader import DataReader
from src.Types import DataType
from lxml import etree as ET


class XmlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        students = {}
        try:
            with open(path, 'r', encoding='windows-1251') as f:  
                tree = ET.parse(f)  
                root = tree.getroot()
        except ET.XMLSyntaxError as e:
            raise ValueError(
                f"Ошибка при парсинге XML: {e}"
            )
        except UnicodeDecodeError as e:
            raise ValueError(
                f"Ошибка кодировки: {e}"
            )

        for student in root.findall('student'):
            student_name = student.get('name')
            if not student_name:
                raise ValueError(
                    "Не найдено имя студента в атрибуте 'name'."
                )

            subjects = []
            for subject in student.findall('subject'):
                subject_name = subject.get('name')
                if not subject_name:
                    raise ValueError(
                        "Не найдено название предмета в атрибуте 'name'."
                    )

                try:
                    score = int(subject.text)
                except ValueError:
                    raise ValueError(
                        f"Ошибка при преобразовании баллов в число для предмета: {subject_name}"
                    )

                subjects.append((subject_name, score))
            students[student_name] = subjects

        return students
