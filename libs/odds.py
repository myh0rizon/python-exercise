import sqlite3
import traceback


def create_record(
        id,
        sport_key,
        sport_nice,
        team_a,
        team_b,
        home_team,
        commence_time) -> bool:

    is_success = True

    try:
        conn = sqlite3.connect('db/betting.sqlite')

        conn.execute(f'INSERT INTO odds \
            (id, sport_key, sport_nice, team_a, team_b, home_team, commence_time) \
            VALUES ("{id}", \
                "{sport_key}", \
                "{sport_nice}", \
                "{team_a}", \
                "{team_b}", \
                "{home_team}", \
                "{commence_time}")')

        conn.commit()
        conn.close()
    except Exception:
        traceback.print_exc()
        is_success = False

    return is_success
