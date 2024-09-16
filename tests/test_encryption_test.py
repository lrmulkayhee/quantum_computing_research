import unittest
import encryption_test

if __name__ == "__main__":
    # Load the tests from encryption_test
    suite = unittest.defaultTestLoader.loadTestsFromModule(encryption_test)
    
    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)