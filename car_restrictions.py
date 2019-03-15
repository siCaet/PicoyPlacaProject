class Car:

    def __init__(self):
        self.plate_num = ''
        self.digit = 0
        self.date = 0
        self.day_week = 0
        self.name = ''
        self.hour = 0
        self.m = 0
        self.restriction_time = ''
        self.car_move = ''

    def get_plate_validation(self):
        import re
        valid_plate = False
        while not valid_plate:
            try:
                plate_let, self.plate_num = input("Plate number in the format AAA-1234: ").split('-')

                if plate_let == [] or self.plate_num == []:
                    print("Incorrect format! empty")
                elif 3 < len(plate_let) or len(plate_let) < 3 or not re.match("^[A-Z]*$", plate_let):
                    print("Incorrect format! three uppercase letters")
                elif 4 < len(self.plate_num) or len(self.plate_num) < 3 or not re.match("^[0-9]*$", self.plate_num):
                    print("Incorrect format! three or four numbers")
                else:
                    valid_plate = True
            except ValueError:
                print("Incorrect format! AAA-1234")

        self.digit = int(self.plate_num[-1])

        return self.digit

    def get_date_validation(self):
        import datetime
        valid_date = False
        while not valid_date:
            date_input = input("Date in the format dd/mm/yy: ")
            try:
                self.date = datetime.datetime.strptime(date_input, "%d/%m/%y")
                valid_date = True
            except ValueError:
                print("Incorrect format! dd/mm/yy")

        self.day_week = self.date.weekday()
        day_names = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
        list_items = day_names.items()
        for item in list_items:
            if item[1] == self.day_week:
                self.name = item[0]

        return self.day_week, self.name

    def get_time_validation(self):
        import datetime
        import time
        valid_time = False
        while not valid_time:
            time_input = input("Time in the format hour,min: ")
            try:
                time1 = time.strptime(time_input, '%H,%M')
                valid_time = True
            except ValueError:
                print("Incorrect format! hour,min")

        time1 = time.strftime('%H:%M', time1)
        self.hour, self.m = time1.split(':')

        time_in = datetime.time(int(self.hour), int(self.m))
        if (datetime.time(7, 0) <= time_in <= datetime.time(9, 30)) or (
                datetime.time(16, 0) <= time_in <= datetime.time(19, 30)):
            self.restriction_time = 1
        else:
            self.restriction_time = 0

        return self.restriction_time

    def transit(self, digit_plate, day_week, restriction_time):

        if (digit_plate == 1 or digit_plate == 2) and day_week == 0:    # Monday
            move = 0
        elif (digit_plate == 3 or digit_plate == 4) and day_week == 1:  # Tuesday
            move = 0
        elif (digit_plate == 5 or digit_plate == 6) and day_week == 2:  # Wednesday
            move = 0
        elif (digit_plate == 7 or digit_plate == 8) and day_week == 3:  # Thursday
            move = 0
        elif (digit_plate == 9 or digit_plate == 0) and day_week == 4:  # Friday
            move = 0
        else:
            move = 1

        if move == 0 and restriction_time == 1:
            self.car_move = "cannot transit"
        else:
            self.car_move = "can transit"

        return self.car_move

    def run_inspection(self):

        plate_dig = self.get_plate_validation()
        day_num, day_name = self.get_date_validation()
        time_restriction = self.get_time_validation()

        move_car = self.transit(plate_dig, day_num, time_restriction)

        print("Last Digit: " + str(plate_dig) + " in " + day_name + " at " + str(self.hour) + ":" + str(
            self.m) + " ==> " + str(move_car))


if __name__ == '__main__':

    import datetime
    import time
    import re
    my_car = Car()

    print("PICO Y PLACA PREDICTOR")

    while True:

        my_car.run_inspection()

