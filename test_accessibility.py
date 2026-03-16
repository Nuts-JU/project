import requests
import time
import json
import argparse

class AccessibilityTester:
    def __init__(self, url, timeout, report_path):
        self.url = url
        self.timeout = timeout
        self.report_path = report_path
        self.results = []

    def validate_url(self):
        # Basic URL validation
        if not self.url.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL format.')
        return True

    def test_accessibility(self):
        session = requests.Session()
        retries = 3
        for i in range(retries):
            try:
                response = session.get(self.url, timeout=self.timeout)
                response.raise_for_status()
                self.results.append({'url': self.url, 'status': 'Accessible', 'status_code': response.status_code})
                return
            except requests.exceptions.RequestException as e:
                print(f'Error accessing {self.url}: {e}')
                if i == retries - 1:
                    self.results.append({'url': self.url, 'status': 'Failed', 'error': str(e)})
                    return
                time.sleep(2)  # wait before retrying

    def print_results(self):
        for result in self.results:
            print(json.dumps(result, indent=4))

    def format_file_size(self, size_bytes):
        if size_bytes < 1024:
            return f'{size_bytes} Bytes'
        elif size_bytes < 1048576:
            return f'{size_bytes / 1024:.2f} KB'
        else:
            return f'{size_bytes / 1048576:.2f} MB'

    def save_report(self):
        with open(self.report_path, 'w') as report_file:
            json.dump(self.results, report_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Test website homepage accessibility.')
    parser.add_argument('url', type=str, help='The URL of the website to test.')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds.')
    parser.add_argument('--report', type=str, default='accessibility_report.json', help='Path to save the report file.')
    args = parser.parse_args()

    tester = AccessibilityTester(args.url, args.timeout, args.report)
    tester.validate_url()
    tester.test_accessibility()
    tester.print_results()
    tester.save_report()

if __name__ == '__main__':
    main()