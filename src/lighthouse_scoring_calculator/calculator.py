from . import metrics
from . import util


class LighthouseScoringCalculator:
    def normalizeVersions(self, version):
        if version == "v9":
            return "v8"
        elif version == "v7":
            return "v6"
        else:
            return version

    def __init__(self, data, device, version):
        self.version = self.normalizeVersions(version)
        self.scoringGuide = metrics.curves[self.version][device]
        self.data = data

        # Check if weights are valid
        weights = [self.scoringGuide[metric]["weight"]
                   for metric in self.scoringGuide]
        assert abs(sum(weights) - 1) <= 0.0001, "Weights do not add up to 1"

        self.log_normalized_values = {}
        for key in self.scoringGuide.keys():
            cuval = self.data[key]
            curve = self.scoringGuide[key]
            if cuval == 0:
                v = 0
            else:
                v = round(util.QUANTILE_AT_VALUE(curve, cuval) * 100) / 100
            self.log_normalized_values[key] = v

    def calc_score(self):
        # Calculate score
        score = round(util.arithmeticMean([(self.log_normalized_values[metric],
                      self.scoringGuide[metric]["weight"]) for metric in self.scoringGuide]) * 100)
        return score

    def get_rating(self, id):
        score = self.log_normalized_values[id]
        RATINGS = {
            'PASS': {'label': 'pass', 'minScore': 0.9},
            'AVERAGE': {'label': 'average', 'minScore': 0.5},
            'FAIL': {'label': 'fail'},
        }

        rating = RATINGS['FAIL']['label']
        if score >= RATINGS['PASS']['minScore']:
            rating = RATINGS['PASS']['label']
        elif score >= RATINGS['AVERAGE']['minScore']:
            rating = RATINGS['AVERAGE']['label']
        return rating

    def get_scoring_guide(self):
        return self.scoringGuide
