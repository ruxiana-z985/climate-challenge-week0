"""
Basic tests for African Climate Trend Analysis project.
"""

import pandas as pd
import numpy as np
import os
import sys

def test_imports():
    """Test that all required packages can be imported."""
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy.stats as stats
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_files_exist():
    """Test that raw data files exist."""
    data_files = [
        'ethiopia.csv',
        'kenya.csv', 
        'sudan.csv',
        'tanzania.csv',
        'nigeria.csv'
    ]
    
    missing_files = []
    for file in data_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing data files: {missing_files}")
        return False
    else:
        print("✅ All raw data files exist")
        return True

def test_notebook_files_exist():
    """Test that all notebook files exist."""
    notebook_files = [
        'notebooks/ethiopia_eda.ipynb',
        'notebooks/kenya_eda.ipynb',
        'notebooks/sudan_eda.ipynb', 
        'notebooks/tanzania_eda.ipynb',
        'notebooks/nigeria_eda.ipynb',
        'notebooks/compare_countries.ipynb'
    ]
    
    missing_files = []
    for file in notebook_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing notebook files: {missing_files}")
        return False
    else:
        print("✅ All notebook files exist")
        return True

def test_pandas_functionality():
    """Test basic pandas functionality."""
    try:
        # Create test dataframe
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
        
        # Test basic operations
        assert len(df) == 5
        assert df['A'].mean() == 3.0
        assert df['B'].std() > 0
        
        print("✅ Pandas functionality test passed")
        return True
    except Exception as e:
        print(f"❌ Pandas test failed: {e}")
        return False

def test_statistical_functions():
    """Test scipy statistical functions."""
    try:
        # Test normal distribution
        data = np.random.normal(0, 1, 1000)
        
        # Test statistical functions
        from scipy import stats
        shapiro_stat, shapiro_p = stats.shapiro(data[:500])
        kruskal_stat, kruskal_p = stats.kruskal(data[:250], data[250:500], data[500:750])
        
        assert isinstance(shapiro_stat, float)
        assert isinstance(shapiro_p, float)
        assert isinstance(kruskal_stat, float)
        assert isinstance(kruskal_p, float)
        
        print("✅ Statistical functions test passed")
        return True
    except Exception as e:
        print(f"❌ Statistical functions test failed: {e}")
        return False

def run_all_tests():
    """Run all basic tests."""
    print("Running Basic Tests for African Climate Analysis")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_data_files_exist,
        test_notebook_files_exist,
        test_pandas_functionality,
        test_statistical_functions
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
            results.append(False)
    
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print(f"⚠️ {total - passed} tests failed")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
