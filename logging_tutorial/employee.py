import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(levelname)s:%(name)s:%(asctime)s::%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# logging.basicConfig(filename='employee.log',
#                     level=logging.INFO, format='%(levelname)s:%(name)s:%(asctime)s::%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

        logger.info(
            'Created Employee: {} - {}'.format(self.fullname, self.email))
        # print('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@domain.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first.title(), self.last.title())


emp_1 = Employee('John', 'Smith')
emp_3 = Employee('Jane', 'Doe')
