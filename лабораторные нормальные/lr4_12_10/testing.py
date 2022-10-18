from claas import Sotrydniki
import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.s1 = Sotrydniki("Зимин Данила Викторович","Лаборант", 2 ,"М","Пушкина 25", "07.07.2002")

    
    def test_account_deposit(self):
        books_city = "Зимин Данила Викторович"
        self.s1.Nama()
        self.assertEqual(self.s1.Nama(), books_city)

if __name__ == '__main__':
    unittest.main()