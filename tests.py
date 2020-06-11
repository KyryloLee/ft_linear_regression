
from classes.read_text_file import ReadTextFile
from train import ModelsTrainer

def print_data_file(data_file : ReadTextFile):
    print(data_file.get_file_content())
    print(data_file.get_file_lines())

def test_read_file():
    data_file = ReadTextFile("./data.csv")
    print_data_file(data_file)

    # empty_data_file = ReadTextFile("")
    # print_data_file(empty_data_file)
    # not_real_data_file = ReadTextFile("./data1.csv")
    # print_data_file(data_file)

test_read_file()
testTrainer = ModelsTrainer("./data.csv")
testTrainer.calculate_linear_regression();
#testTrainer.show_visualisation()