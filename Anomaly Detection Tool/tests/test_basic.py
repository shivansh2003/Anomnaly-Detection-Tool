# --------------------------- tests/test_basic.py ---------------------------
import unittest
import pandas as pd
from analyzer.analyze import analyze_traffic

class TestAnalyzer(unittest.TestCase):
    def test_analysis(self):
        test_data = pd.DataFrame({
            'Source': ['A', 'A', 'B'],
            'Destination': ['B', 'B', 'C'],
            'Protocol': ['TCP', 'TCP', 'UDP'],
            'Length': [100, 150, 200]
        })
        result = analyze_traffic(test_data)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()

# --------------------------- main.py ---------------------------
from cli.main_cli import main

if __name__ == '__main__':
    main()
