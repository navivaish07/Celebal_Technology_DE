from pathlib import Path
import database

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / 'sql'
REPORTS_DIR = ROOT / 'reports'
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def read_sql(path):
    return path.read_text(encoding='utf-8')


def export_results():
    if not database.DB_PATH.exists():
        database.load_cleaned_data()

    conn = database.connect_db()
    report_path = REPORTS_DIR / 'sql_analysis_results.txt'
    with report_path.open('w', encoding='utf-8') as fout:
        for sql_file in sorted(SQL_DIR.glob('*.sql')):
            query_text = read_sql(sql_file).strip()
            fout.write(f'-- {sql_file.name}\n')
            fout.write(query_text + '\n\n')
            try:
                rows = conn.execute(query_text).fetchall()
                if rows:
                    headers = rows[0].keys()
                    fout.write('| ' + ' | '.join(headers) + ' |\n')
                    fout.write('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')
                    for row in rows[:20]:
                        fout.write('| ' + ' | '.join(str(row[h]) for h in headers) + ' |\n')
                else:
                    fout.write('No rows returned.\n')
            except Exception as exc:
                fout.write(f'Query failed: {exc}\n')
            fout.write('\n')
    conn.close()
    print(f'Query results written to {report_path}')


if __name__ == '__main__':
    export_results()
