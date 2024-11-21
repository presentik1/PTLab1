from src.DataReader import DataReader
from src.Types import DataType
from lxml import etree as ET
from charset_normalizer import from_path  # Для автоматического определения кодировки


class XmlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        students = {}
        try:
            # Определение кодировки файла
            detected_encoding = from_path(path).best().encoding

            with open(path, 'r', encoding=detected_encoding) as f:
                tree = ET.parse(f)  # Парсинг XML файла
                root = tree.getroot()
        except ET.XMLSyntaxError as e:
            raise ValueError(f"Ошибка при парсинге XML: {e}")
        except UnicodeDecodeError as e:
            raise ValueError(f"Ошибка кодировки: {e}")
        except Exception as e:
            raise ValueError(f"Произошла непредвиденная ошибка: {e}")

        for student in root.findall('student'):
            student_name = student.get('name')
            if not student_name:
                raise ValueError("Не найдено имя студента в атрибуте 'name'.")

            subjects = []
            for subject in student.findall('subject'):
                subject_name = subject.get('name')
                if not subject_name:
                    raise ValueError("Не найдено название предмета в атрибуте 'name'.")

                try:
                    score = int(subject.text)
                except (ValueError, TypeError):
                    raise ValueError(
                        f"Ошибка преобразования баллов в число для предмета: {subject_name}"
                    )

                subjects.append((subject_name, score))
            students[student_name] = subjects

        return students
