
while True:
    try:
        number = int(input("Enter a number of ur choice :\n"))
        print(18/number)
        break
    except ValueError:
        print("Make Sure and Enter Correct Number")
    except ZeroDivisionError:
        print("Don't divide by zero")
    except:
        break
    finally:
        print("Print no matter what")

