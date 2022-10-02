from lighthouse_scoring_calculator import LighthouseScoringCalculator
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Calculate the score and rating of each metric\nExample: $ python3 -m lighthouse_scoring_calculator -d mobile -v v9 --fcp 2130 --si 5800 --fmp 4000 --tti 7300 --fci 6500 --lcp 4000 --tbt 600 --cls 0.25',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--device', help='The device type',
                        required=False, default='mobile')
    parser.add_argument(
        '-v', '--version', help='The lighthouse version', required=False, default='v9', type=str)
    parser.add_argument(
        '--fcp', help='The First Contentful Paint metric', required=False, default=0, type=float)
    parser.add_argument('--si', help='The Speed Index metric',
                        required=False, default=0, type=float)
    parser.add_argument(
        '--fmp', help='The First Meaningful Paint metric', required=False, default=0, type=float)
    parser.add_argument(
        '--tti', help='The Time to Interactive metric', required=False, default=0, type=float)
    parser.add_argument(
        '--fci', help='The First CPU Idle metric', required=False, default=0, type=float)
    parser.add_argument(
        '--lcp', help='The Largest Contentful Paint metric', required=False, default=0, type=float)
    parser.add_argument(
        '--tbt', help='The Total Blocking Time metric', required=False, default=0, type=float)
    parser.add_argument(
        '--cls', help='The Cumulative Layout Shift metric', required=False, default=0, type=float)
    args = parser.parse_args()

    data = {
        "FCP": args.fcp,
        "SI": args.si,
        "FMP": args.fmp,
        "TTI": args.tti,
        "FCI": args.fci,
        "LCP": args.lcp,
        "TBT": args.tbt,
        "CLS": args.cls
    }

    calculator = LighthouseScoringCalculator(data, args.device, args.version)
    scoringGuide = calculator.get_scoring_guide()
    print("Score:", calculator.calc_score())
    for metric in scoringGuide:
        print(f"Rating of {metric}:", calculator.get_rating(metric))


if __name__ == "__main__":
    main()
