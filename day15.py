# try:
#     a = "1"
#     int(a)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except ValueError:
#     print("Value Error")
# except:
#     print("Something went wrong")

# finally:
#     print("Completed")


# try:
#     print(1/0)
#     a = "1"
#     int(a)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)

# finally:
#     print("Completed")


# f = open("day1.py", "r")
# print(f.read())


# f = open("day1.py", "a")
# print(f.write("Hello"))



# try:
#     print(a)
#     print(1 / 0)
#     a = "1"
#     int(a)
# except ZeroDivisionError as e:
#     f = open("zerodivison.txt", "w")
#     print(f.write("Zero divison error"))
#     f.close()
# except ValueError as e:
#     f = open("value_error.txt", "w")
#     print(f.write("Value Error"))
#     f.close()
# except Exception as e:
#     f = open("exception.txt", "w")
#     print(f.write("Something went wrong"))
#     f.close()


# finally:
#     print("Completed")


def error_message(file_name, message):
    f = open(file_name,"a")
    f.write(message )
    f.close()
    return True


try:
    print(a)
    print(1 / 0)
    a = "1"
    int(a)
except ZeroDivisionError as e:
   error_message("zerodivision.txt", str(e))
except ValueError as e:
    error_message("value_error.txt", str(e))
except Exception as e:
   error_message("exception.txt", str(e))


finally:
    print("Completed")



with open('day2.py','r') as f:
    print(f.read())