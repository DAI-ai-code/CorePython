def replace_data_in_file(file, source, destination):
    file = open("prog6_ans.txt", "r")
    data = file.read()
    file.close()
    data.replace(source, destination)
    file = open("prog6_ans.txt", "w")
    file.write(data)
    file.close()


try:
    file = open("prog6_ans.txt", "w")
    file.write("this is a test file\ntesting")
    file.close()
    file = open("prog6_ans.txt", "r")
    data = file.read()
    file.close()
    file = open("prog6_ans.txt", "w")
    file.write(data.replace("test", "TEST"))
finally:
    file.close()



    # f = open("prog6_source.txt", 'w')
    # f.write('written')
    # f.close()
    # f = open("prog6_destination.txt", "w")
    # f.write("created")
    # f.close()
    # f = open("prog6_ans.txt", 'w')
    # f.write('this is a sentence written')
    # f.close()
    # #
    # f = open('prog6_source.txt', 'r+')
    # source_word = f.read()
    # f.close()
    # f = open('prog6_destination.txt', 'r')
    # destination_word = f.read()
    # f.close()
    # f = open("prog6_ans.txt", 'w')
    # data = f