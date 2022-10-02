from lighthouse_scoring_calculator import LighthouseScoringCalculator

testData = {
    "FCP": 2130,
    "SI": 5800,
    "FMP": 4000,
    "TTI": 7300,
    "FCI": 6500,
    "LCP": 4000,
    "TBT": 600,
    "CLS": 0.25
}

calculator = LighthouseScoringCalculator(testData, "mobile", "v9")

print("Score:", calculator.calc_score())
print("Rating of FCP:", calculator.get_rating("FCP"))
