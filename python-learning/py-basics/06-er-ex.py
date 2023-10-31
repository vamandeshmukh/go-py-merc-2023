
print('start')

# try:
#     output = 10 / 0
#     print(output)
# except (ZeroDivisionError) as ex:
#     print(ex)
# finally:
#     print('done')

nums = [2, 8, 0, 5, 3]
try:
    output = 10 / nums[3]
    print(output)
except (ZeroDivisionError, IndexError) as ex:
    print(ex)
finally:
    print('done')




print('end')