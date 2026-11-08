import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

health=load('health', 'projects/infra-health/healthcheck.py')
incident=load('incident', 'projects/incident-insights/analyze.py')
backup=load('backup', 'projects/backup-integrity/integrity.py')
headers=load('headers', 'projects/security-headers/review.py')

class PortfolioTools(unittest.TestCase):
    def test_disk_status(self):
        r=health.disk_status('.', 100)
        self.assertIn('available_gb', r)
        self.assertLessEqual(r['used_percent'], 100)

    def test_incident_metrics(self):
        r=incident.analyze(ROOT / 'projects/incident-insights/data/incidents.csv')
        self.assertEqual(r['total'], 6)
        self.assertEqual(r['by_priority']['high'], 2)

    def test_integrity_changes(self):
        with tempfile.TemporaryDirectory() as d:
            f=pathlib.Path(d)/'sample.txt'
            f.write_text('original',encoding='utf-8')
            m=backup.manifest(f)
            self.assertTrue(backup.verify(f,m))
            f.write_text('changed',encoding='utf-8')
            self.assertFalse(backup.verify(f,m))

    def test_headers_normalized(self):
        r=headers.review({'CONTENT-SECURITY-POLICY':'default-src self'})
        self.assertIn('content-security-policy',r['present'])
        self.assertIn('strict-transport-security',r['missing'])

if __name__=='__main__':
    unittest.main()
