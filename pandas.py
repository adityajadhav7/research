import pandas as pd

data = pd.read_csv('data.csv')


data.describe()

data.info()


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna({'quantity':0})

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df = students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'})
    return df

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 2 * employees['salary'] 
    return employees


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)


student_data = [[1, 15],[2, 11],[3, 11],[4, 20]]

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    result = pd.DataFrame(student_data, columns=("student_id", "age"))
    return result

createDataframe(student_data)
