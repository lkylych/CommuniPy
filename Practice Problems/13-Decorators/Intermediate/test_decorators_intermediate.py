from unittest import TestCase, TestSuite, TextTestRunner, main


class DecoratorsIntermediateTestCase(TestCase):
    pass


def test_one(test_name):
    suite = TestSuite()
    suite.addTest(DecoratorsIntermediateTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
