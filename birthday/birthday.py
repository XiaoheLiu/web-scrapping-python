import datetime as dt


class Birthday:
    """
    Calculate and print days and dates about birthdays.
    """

    def __init__(self, year=None, month=None, day=None):
        self.birthday = dt.date(year, month, day)

    def days_existed(self):
        """
        Calculate how many days this person has existed.
        Returns:
            Days existed (int)
        """
        td = dt.date.today()
        days_lived = (td-self.birthday).days
        print(f'You have lived {days_lived} days!')
        return days_lived

    def calculate_nearest_birthday(self):
        """
        Calculate the nearest birthday. (For leap year babies, Feb 28 is considered as birthday if the year of their next birthday is not leap.)
        Returns:
            A date object 
        """
        td = dt.date.today()
        try:
            bday_this_year = dt.date(
                td.year, self.birthday.month, self.birthday.day)
        except ValueError:
            bday_this_year = dt.date(td.year, 2, 28)
        if td <= bday_this_year:
            return bday_this_year
        else:
            try:
                bd_next_year = dt.date(
                    td.year+1, self.birthday.month, self.birthday.day)
            except ValueError:
                bd_next_year = dt.date(td.year+1, 2, 28)
            return bd_next_year

    def nearest_birthday(self):
        """
        Print out the person's nearest birthday
        Returns:
            None
        """
        nearest_bd = self.calculate_nearest_birthday()
        print(
            f'Your next birthday is on {nearest_bd:%A, %B %d, %Y}.')

    def days_to_next_birthday(self):
        """
        Calculate and print out the days to next birthday
        Returns:
            days to the next birthday (int)
        """
        next_bd = self.calculate_nearest_birthday()
        days_left = (next_bd - dt.date.today()).days
        print(f'Your next birthday is in {days_left} days!')
        return days_left

    def __str__(self):
        return f'You were born on {self.birthday:%A, %B %d, %Y}.'


if __name__ == '__main__':
    s = input("Enter your birthday in the format of YYYY-MM-DD: ")
    dates = [int(n) for n in s.split('-')]
    bd = Birthday(*dates)
    print(bd)
    bd.days_existed()
    bd.nearest_birthday()
    bd.days_to_next_birthday()
