from matplotlib import pyplot as plt



def view_graph(dataset):
    print(dataset)
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    labels = ['orX', 'orY', 'orZ', 'rX', 'rY', 'rZ', 'accX', 'accY', 'accZ', 'mX', 'mY', 'mZ', 'gX', 'gY', 'gZ']

    def pie_chart(abs_data, title):
        plt.xticks(x)
        plt.title(title)
        patches, texts = plt.pie(abs_data, startangle=90)
        plt.legend(patches, labels, bbox_to_anchor=(1, 0), loc="lower right", bbox_transform=plt.gcf().transFigure)
        plt.show()

    def line_chart(abs_data, title):
        plt.xticks(x, labels)
        plt.title(title)
        plt.plot(abs_data, label='')
        plt.xlabel('sensors')
        plt.ylabel('features')
        plt.show()

    def bar_chart(abs_data, title):
        print(abs_data)
        plt.xticks(x, labels)
        print('hi')
        plt.title(title)
        plt.xlabel('sensors')
        plt.ylabel('features')
        plt.bar(x, abs_data)
        plt.show()

    def scatter_chart(abs_data, title):
        plt.xticks(x, labels)
        plt.title(title)
        plt.xlabel('sensors')
        plt.ylabel('features')
        plt.scatter(x, abs_data)
        plt.show()

    def hist_chart(abs_data, title):
        plt.figure(figsize=(8, 4))
        plt.title(title)
        plt.xticks(x, labels)
        plt.xlabel('sensors')
        plt.ylabel('features')
        plt.hist(abs_data)
        plt.show()

    for data in dataset:
        print(data)
        title = data[0]
        choice = input('Do you wanna generate graphs for ' + title + ' data(y/n): ')
        if choice == 'y' or choice == 'yes':
            del data[0]
            abs_data = [abs(row) for row in data]
            pie_chart(abs_data=abs_data, title=title)
            line_chart(abs_data=abs_data, title=title)
            bar_chart(abs_data=abs_data, title=title)
            scatter_chart(abs_data=abs_data, title=title)
            hist_chart(abs_data=abs_data, title=title)
        else:
            print('Data generation skipped for ' + title + ' data')

        show_graph(dataset)

def show_graph(dataset):
    choice = input('Do you wanna view the graph for the data set(y/n): ')
    if choice == 'y' or choice == 'yes':
        print('----------------program started---------------')
        view_graph(dataset)
    else:
        print('-------------Program ended------------')

# data_set = [
#     ['Mean', 126.7, -17.0, 2.0, 0.06995357, -0.13229000000000002, -0.8800488999999999, 0.11492176000000003, 2.68151,
#      8.657430000000002, -31.199999999999996, -35.720000000000006, -36.92, -0.03520796, 2.6806049999999995,
#      8.653112999999998],
#     ['Median', 126.0, -17.0, 2.0, 0.0671819, -0.133712, -0.882605, -0.0383072, 2.68151, 8.65743, -31.2, -36.0, -37.2,
#      -0.0568672, 2.67834, 8.64654],
#     ['standard_deviation', 0.6403124237432847, 0.0, 0.0, 0.0015983583503394992, 0.0008260167068528297,
#      0.0017662029583261245, 0.07661448, 0.0, 1.7763568394002505e-15, 3.552713678800501e-15, 0.18330302779823293,
#      0.3600000000000017, 0.022647581451711352, 0.0018004513323052888, 0.0050302088425832146],
#     ['covarience', 0.5053768143198775, -0.0, 0.0, 2.284884603229684, -0.6243984479951845, -0.2006937294423213,
#      66.66664346247393, 0.0, 2.0518292835174527e-14, -1.1386902816668274e-14, -0.5131663712156576, -0.9750812567714022,
#      -64.32517377238372, 0.06716585742044386, 0.05813178266114422],
#     ['root_mean_square', 253.4, -34.0, 4.0, 0.13990714, -0.26458000000000004, -1.7600977999999998, 0.22984352000000005,
#      5.36302, 17.314860000000003, -62.39999999999999, -71.44000000000001, -73.84, -0.07041592, 5.361209999999999,
#      17.306225999999995],
#     ['sum_of_squares', 160533.0, 2890.0, 40.0, 0.04896056705161, 0.17501326403599998, 7.744891858641, 0.19076789467168,
#      71.904958801, 749.5109420489999, 9734.4, 12759.520000000004, 13632.159999999998, 0.017525133929734996,
#      71.8564640765, 748.7638989377]]
