def slices(string, series):

    digit_list = [int(digit) for digit in string]

    if series > len(string):
        raise ValueError("Error: The sequence is larger than the string!")

    return [digit_list[i:series + i] for i in range(len(digit_list)) if series + i <= len(digit_list)]


def largest_product(string, series):

    output_value = 1

    if string != "":
        series_list = slices(string, series)
        for sequence in series_list:
            temp_value = sequence[0] * sequence[1]
            for index, value in enumerate(sequence):
                if index <= (len(sequence)-1) and index > 1:
                    if temp_value > 0:
                        temp_value = temp_value * value
            else:
                if temp_value > output_value:
                    output_value = temp_value
    return output_value
