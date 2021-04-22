import math
import time
import csv
from load_dataset_module import activity_features




def feature_module(file):
    final_dict = {}

    # eight functions
    def find_mean(numbers):
        length = len(numbers)
        result = sum(numbers) / length
        return result

    def find_median(numbers):
        list_n = sorted(numbers)
        if len(list_n) % 2 == 0:
            a = (len(list_n) // 2) - 1
            b = (len(list_n) // 2)
            median = (list_n[a] + list_n[b]) / 2
        else:
            median = list_n[len(list_n) // 2]
        return median

    def find_varience(numbers):
        length = len(numbers)
        mean_result = find_mean(numbers)
        square_diff = []
        for number in numbers:
            square_diff.append((number - mean_result) ** 2)
        result = sum(square_diff) / length
        return result

    def find_standard_deviation(numbers):
        varience_result = find_varience(numbers)
        return varience_result ** 0.5

    def find_covarience(numbers):
        standard_deviation_result = find_standard_deviation(numbers)
        covarience = (standard_deviation_result / find_mean(numbers)) * 100
        return covarience

    def find_root_mean_square(numbers):
        square_list = []
        for num in numbers:
            square_list.append(num ** 2)
        mean = sum(square_list) / len(numbers)
        return math.sqrt(mean)

    def find_sum_of_squares(numbers):
        square_list = []
        for number in numbers:
            square_list.append(number ** 2)
        return sum(square_list)

    def find_zero_cross(numbers):
        count_array = []
        for index in range(0, len(numbers) - 1):
            if numbers[index] * numbers[index + 1] < 0:
                count_array.append(1)
            elif numbers[index] * numbers[index + 1] > 0:
                count_array.append(0)
        return sum(count_array)

    def collect_features(numbers):
        return {'mean': find_mean(numbers), 'median': find_median(numbers), 'varience': find_varience(numbers),
                'standard_deviation': find_standard_deviation(numbers), 'covarience': find_covarience(numbers),
                'root_mean_square': find_root_mean_square(numbers), 'sum_of_squares': find_sum_of_squares(numbers),
                'zero_cross': find_zero_cross(numbers)}

    # end of functions

    activity_data_result = activity_features(file)

    for item, values in activity_data_result.items():
        final_dict[item] = collect_features(values)
    output_file_name = input('Please type a output file name(eg:"result"): ')
    with open(output_file_name + '.csv', 'w', newline='') as features_csv:
        csv_headers = ['feature', 'orX', 'orY', 'orZ', 'rX', 'rY', 'rZ', 'accX', 'accY', 'accZ', 'mX', 'mY', 'mZ', 'gX',
                       'gY', 'gZ', 'soundLevel']
        writer = csv.writer(features_csv)
        mean = ['Mean']
        median = ['Median']
        varience = ['varience']
        standard_deviation = ['standard_deviation']
        covarience = ['covarience']
        root_mean_square = ['root_mean_square']
        sum_of_squares = ['sum_of_squares']
        zero_cross = ['zero_cross']
        for item, val in final_dict.items():
            mean.append(val['mean'])
            median.append(val['median'])
            varience.append(val['varience'])
            standard_deviation.append(val['standard_deviation'])
            covarience.append(val['covarience'])
            root_mean_square.append(val['root_mean_square'])
            sum_of_squares.append(val['sum_of_squares'])
            zero_cross.append(val['zero_cross'])

        writer.writerow(csv_headers)
        writer.writerow(mean)
        writer.writerow(median)
        writer.writerow(varience)
        writer.writerow(standard_deviation)
        writer.writerow(covarience)
        writer.writerow(root_mean_square)
        writer.writerow(sum_of_squares)
        writer.writerow(zero_cross)

        time.sleep(1)
        print('Data processed successfully')
        time.sleep(1)
        print('Data saved successfully in ' + output_file_name + '.csv')
        main(text="Do you wanna run the program again(y/n): ")


def main(text):
    time.sleep(1)
    print(text)
    selection = input(": ")
    if selection == 'y' or selection == 'yes':
        feature_module(file='smallData.csv')
    else:
        time.sleep(1)
        print('-----------Program Ended--------- ')


print('Human Activity Recognition  systems') 
print('Welcome to Human activity recognition System , We helps you calculate accurate and fast statistical features '
      'of your data ')
print('--------------------------------------------------------------------------')
main(text="Do you wanna start(y/n): ")
