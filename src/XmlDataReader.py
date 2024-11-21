from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET

class XmlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        students = {}
        tree = ET.parse(path)
        root = tree.getroot()
        for student in root:
            student_name = student.tag
            subjects = []
            for subject in student:
                subjects.append((subject.tag, int(subject.text)))
            students[student_name] = subjects
        return students
