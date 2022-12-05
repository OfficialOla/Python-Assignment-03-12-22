# def celcius_to_fahr(cel_val):
#     """
#     This fuction to convert celcius temp to fahr temp.
#     :param cel_val: float
#     :return: float
#     # >>> celcius_to_fahr(16)
#     60.8
#      # >>> celcius_to_fahr(23)
#     73.4
#     """
#     fahr = cel_val * 1.8 + 32.0
#     return fahr
#
#
# cal = float(input("enter number dummy!  "))
# print(celcius_to_fahr(cal))

#     def is_unique(lst, number=None):
#         duplicates = [number for number in number if number.count(number) > 1]
#         number = [1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2]
#         is_unique = list(set(duplicates))
#     print(not is_unique)
# # return [2, 3, 4]
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:

            return max_num