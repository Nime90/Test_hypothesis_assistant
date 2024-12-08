def run_test(data,test_name,dependent_variable,independent_variable):
    from Tests.OneWayAnova import OneWayAnova
    from Tests.SimpleRegression import SimpleRegression
    from Tests.McNemarTest import McNemarTest
    from Tests.WilcoxonSignedRankSumTest import WilcoxonSignedRankSumTest
    from Tests.MultivariateMultipleregression import MultivariateMultipleregression
    from Tests.OneWayRepeatedMeasuresAnova import OneWayRepeatedMeasuresANOVA
    from Tests.NonParametricCorrelation import NonParametricCorrelation
    from Tests.OrderedLogisticRegression import OrderedLogisticRegression 
    from Tests.SimpleLogisticRegression import SimpleLogisticRegression
    from Tests.ChiSquareGoodnessOfFit import ChisquareGoodnessOfFit
    from Tests.OneSampleMedianTest import OneSampleMediantest
    from Tests.MultipleLogisticRegression import MultipleLogisticRegression
    from Tests.FactorialLogisticRegression import FactorialLogisticRegression
    from Tests.KruskalWallisTest import KruskalWallis
    from Tests.RepeatedMeasuresLogisticRegressions import RepeatedMeasuresLogisticRegression
    from Tests.OneSampleTtest import OneSampleTtest
    from Tests.PairedSampleTtest import PairedSamplesTtest
    from Tests.FriedmanTest import FriedmanTest
    from Tests.MultipleRegression import MultipleRegression
    from Tests.OneWayManova import OneWayManova

    test_of_h = None
    if 'TwoIndependentSampleTtest.py' in str(test_name) and dependent_variable and independent_variable:
        from Tests.TwoIndependentSampleTtest import IndSamplesTtest as TwoIndependentSampleTtest
        test_of_h = TwoIndependentSampleTtest(data, column1=dependent_variable, column2=independent_variable[0], P_value=0.05, tails=2)
    
    elif 'FactorialAnova.py' in str(test_name) and dependent_variable and independent_variable:
        from Tests.FactorialAnova import FactorialANOVA
        test_of_h = FactorialANOVA(data, dependent_variable, independent_variable)
   
    elif 'AnalysisOfCovariance.py' in str(test_name) and dependent_variable and independent_variable:
        from Tests.AnalysisOfCovariance import AnalysisOfCovariance
        test_of_h = AnalysisOfCovariance(data, dependent_variable, independent_variable)
    
    elif 'ChiSquare.py' in str(test_name) and dependent_variable and independent_variable:
        from Tests.ChiSquare import Chisquare
        test_of_h = Chisquare(data, independent_variable[0], dependent_variable, P_value=0.05)
    
    elif 'BinomialTest.py' in str(test_name) and dependent_variable:
        from Tests.BinomialTest import BinomialTest
        test_of_h = BinomialTest(data, dependent_variable)
    
    elif 'Correlation.py' in str(test_name) and dependent_variable and independent_variable:
        from Tests.Correlation import correlation
        test_of_h = correlation( data, dependent_variable, independent_variable[0] )

    elif 'WilcoxonMannWhitneyTest' in str(test_name) and dependent_variable and independent_variable:
        from Tests.WilcoxonMannWhitneyTest import IndSamplesTtest_WMW as WilcoxonMannWhitneyTest
        test_of_h = WilcoxonMannWhitneyTest(data, column1=dependent_variable, column2=independent_variable[0], P_value=0.05, tails=2)

    return test_of_h